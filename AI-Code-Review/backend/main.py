from fastapi import FastAPI
from models import CodeInput
from reviewer import get_review

app = FastAPI()

@app.post("/review")
async def review(data: CodeInput):

    result = get_review(data.code)

    return {
        "review": result
    }