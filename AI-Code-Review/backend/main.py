from fastapi import FastAPI
from models import CodeInput
from reviewer import get_review
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.post("/review")
async def review(data: CodeInput):

    result = get_review(data.code)

    return result
   


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)