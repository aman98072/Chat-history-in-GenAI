from fastapi import APIRouter
from app.models.schemas import ChatRequest
from app.services.chat import chat

router = APIRouter()

@router.post('/chat')
def chatBot(request: ChatRequest):
    text = request.text
    id = request.id

    response = chat(text, id)
    return response

