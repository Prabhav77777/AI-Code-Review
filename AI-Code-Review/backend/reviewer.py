from groq import Groq
from dotenv import load_dotenv
from json_repair import repair_json
import os
import json

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL = "llama-3.3-70b-versatile"
MAX_TOKENS = 4096


def _build_prompt(code):
    return f"""
You are an expert code reviewer.

Analyze the code and return ONLY valid JSON.

IMPORTANT:
- Do not use markdown.
- Do not use ```json.
- Do not include explanations.
- Return exactly one JSON object with EXACTLY these keys: score, issues, suggestions, optimized_code.
- score must be a number between 0 and 10.
- issues must be a list of strings.
- suggestions must be a list of strings.
- optimized_code must be a string containing the improved code.
- Inside optimized_code, all double quotes, backslashes, and newlines MUST be
  properly JSON-escaped (\\", \\\\, \\n) so the result is valid JSON.

JSON format:

{{
  "score": 0,
  "issues": [],
  "suggestions": [],
  "optimized_code": ""
}}

Code:
{code}
"""


def _call_groq(code, force_json_mode=True):
    kwargs = {
        "model": MODEL,
        "max_tokens": MAX_TOKENS,
        "temperature": 0.2,
        "messages": [
            {
                "role": "user",
                "content": _build_prompt(code)
            }
        ]
    }

    if force_json_mode:
        # Groq's JSON mode forces the model to emit a single, syntactically
        # valid JSON object (with properly escaped strings), which fixes the
        # vast majority of parsing failures caused by code containing quotes,
        # backslashes, etc.
        kwargs["response_format"] = {"type": "json_object"}

    response = client.chat.completions.create(**kwargs)
    return response.choices[0].message.content, response.choices[0].finish_reason


def _extract_json(raw_text):
    """
    Try to turn raw_text into a JSON object.

    1. Try json.loads directly.
    2. Fall back to slicing between the first '{' and last '}'.
    3. Fall back to json_repair, which can fix common issues like
       unescaped quotes, trailing commas, truncated strings, etc.
    """
    candidates = [raw_text]

    start = raw_text.find("{")
    end = raw_text.rfind("}") + 1
    if start != -1 and end > start:
        candidates.append(raw_text[start:end])

    for candidate in candidates:
        try:
            return json.loads(candidate)
        except Exception:
            continue

    # Last resort: repair the most promising candidate.
    target = candidates[-1] if len(candidates) > 1 else candidates[0]
    repaired = repair_json(target)
    return json.loads(repaired)


def _normalize_result(data, fallback_code):
    """
    Make sure the result always has the expected shape/types,
    regardless of what the model returned.
    """
    score = data.get("score", 0)
    try:
        score = float(score)
    except (TypeError, ValueError):
        score = 0
    score = max(0, min(10, score))

    issues = data.get("issues", [])
    if not isinstance(issues, list):
        issues = [str(issues)] if issues else []
    issues = [str(i) for i in issues]

    suggestions = data.get("suggestions", [])
    if not isinstance(suggestions, list):
        suggestions = [str(suggestions)] if suggestions else []
    suggestions = [str(s) for s in suggestions]

    optimized_code = data.get("optimized_code", fallback_code)
    if not isinstance(optimized_code, str) or not optimized_code.strip():
        optimized_code = fallback_code

    return {
        "score": score,
        "issues": issues,
        "suggestions": suggestions,
        "optimized_code": optimized_code
    }


def _service_unavailable(code):
    return {
        "score": 0,
        "issues": ["AI service unavailable"],
        "suggestions": ["Please try again later"],
        "optimized_code": code
    }


def _parsing_failed(code):
    return {
        "score": 0,
        "issues": ["AI parsing failed"],
        "suggestions": ["Try submitting the code again"],
        "optimized_code": code
    }


def get_review(code):
    last_error = None

    # Attempt 1: JSON mode (preferred). Attempt 2: plain mode, in case the
    # JSON-mode request itself errors out for some reason (e.g. unsupported
    # combination of params).
    for attempt, force_json_mode in enumerate([True, False]):
        try:
            review, finish_reason = _call_groq(code, force_json_mode=force_json_mode)
        except Exception as e:
            print("Groq Error:", e)
            last_error = e
            continue

        if finish_reason == "length":
            print("Groq response was truncated (finish_reason=length)")

        try:
            parsed = _extract_json(review)
            return _normalize_result(parsed, code)
        except Exception as e:
            print("JSON Parse Error:", e)
            print("Raw AI Response:")
            print(review)
            last_error = e
            continue

    if last_error is not None and not isinstance(last_error, (ValueError, json.JSONDecodeError)):
        return _service_unavailable(code)

    return _parsing_failed(code)