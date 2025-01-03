from fastapi import APIRouter
from backend.interactors import chat as chat_interactor

# Create a router.
router = APIRouter(tags=['chat'],prefix="/api")

@router.get("/chat/")
async def chat(question:str):
    return chat_interactor.call(question)