from fastapi import FastAPI, Request
from pydantic import BaseModel
from app.chat import ask_llm
import traceback

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat_endpoint(req: ChatRequest):
    try:
        reply = ask_llm(req.message)
        return {"response": reply}
    except Exception as e:
        traceback.print_exc()
        return {"error": str(e)}
