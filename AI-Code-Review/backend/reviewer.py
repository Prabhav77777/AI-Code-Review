from groq import Groq
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def get_review(code):

    prompt = f"""
You are an expert code reviewer.

Analyze the code and return ONLY valid JSON.

IMPORTANT:
- Do not use markdown.
- Do not use ```json.
- Do not include explanations.
- Return exactly one JSON object.
- score must be between 0 and 10.
- issues must be a list of strings.
- suggestions must be a list of strings.
- optimized_code must contain improved code.

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

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        review = response.choices[0].message.content

    except Exception as e:
        print("Groq Error:", e)

        return {
            "score": 0,
            "issues": ["AI service unavailable"],
            "suggestions": ["Please try again later"],
            "optimized_code": code
        }

    try:
        start = review.find("{")
        end = review.rfind("}") + 1

        review_json = review[start:end]

        return json.loads(review_json)

    except Exception as e:
        return {
            "score": 0,
            "issues": [
                "JSON Parse Error",
                str(e)
            ],
            "suggestions": [],
            "optimized_code": review
        }