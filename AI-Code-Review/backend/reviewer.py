from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def get_review(code):

    prompt = f"""
Review this code.

Return ONLY in this format:

Code Quality Score: X/10

Issues Found:
- issue 1
- issue 2

Suggestions:
- suggestion 1
- suggestion 2

Optimized Code:
<improved code>

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

    return response.choices[0].message.content
