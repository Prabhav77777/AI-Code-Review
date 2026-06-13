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

Rules:
- Return no explanation outside JSON.
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

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    review=response.choices[0].message.content
    try:
        return json.loads(review)

    except:
        return {
        "score": 0,
        "issues": ["AI parsing failed"],
        "suggestions": [],
        "optimized_code": code
    }
