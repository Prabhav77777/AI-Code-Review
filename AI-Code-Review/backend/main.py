from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class CodeRequest(BaseModel):
    code:str
@app.post("/review")
def review_code(data:CodeRequest):
    return {
        "received":len(data.code)
    }