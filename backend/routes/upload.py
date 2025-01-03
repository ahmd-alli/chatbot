from fastapi import APIRouter, UploadFile, File
from backend.interactors import upload as upload_interactor

# Create a router.
router = APIRouter(tags=['chat'],prefix="/api")

# Routes.
@router.post("/upload-knowledge/")
async def upload_knowledge(file: UploadFile = File(...)):
    content = await file.read()
    return upload_interactor.call(content, file.filename)
