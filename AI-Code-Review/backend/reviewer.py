from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def get_review(code):

    prompt = f"""
You are an expert code reviewer.

Return your response in EXACTLY this format:

SCORE:
<number>

ISSUES:
- issue 1
- issue 2

SUGGESTIONS:
- suggestion 1
- suggestion 2

OPTIMIZED_CODE:
<full optimized code>

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

        print("AI RESPONSE:")
        print(review)

    except Exception as e:
        print("Groq Error:", e)

        return {
            "score": 0,
            "issues": ["AI service unavailable"],
            "suggestions": ["Please try again later"],
            "optimized_code": code
        }

    try:

        # SCORE
        score_text = review.split("SCORE:")[1].split("ISSUES:")[0].strip()
        score = int(score_text)

        # ISSUES
        issues_text = review.split("ISSUES:")[1].split("SUGGESTIONS:")[0]

        issues = [
            line.replace("-", "").strip()
            for line in issues_text.split("\n")
            if line.strip().startswith("-")
        ]

        # SUGGESTIONS
        suggestions_text = review.split("SUGGESTIONS:")[1].split("OPTIMIZED_CODE:")[0]

        suggestions = [
            line.replace("-", "").strip()
            for line in suggestions_text.split("\n")
            if line.strip().startswith("-")
        ]

        # OPTIMIZED CODE
        optimized_code = review.split("OPTIMIZED_CODE:")[1].strip()

        return {
            "score": score,
            "issues": issues,
            "suggestions": suggestions,
            "optimized_code": optimized_code
        }

    except Exception as e:

        print("Parsing Error:", e)
        print(review)

        return {
            "score": 0,
            "issues": ["Response parsing failed"],
            "suggestions": ["Try again"],
            "optimized_code": review
        }