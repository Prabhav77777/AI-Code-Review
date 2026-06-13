from fastapi import FastAPI
from models import CodeInput
from reviewer import get_review
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.post("/review")
async def review(data: CodeInput):
    return {
    "score": 8,
    "issues": [
        "Missing comments"
    ],
    "suggestions": [
        "Add comments"
    ],
    "optimized_code": data.code
}
   

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)