import os
from backend.service.pinecone import PineconeDB
from backend.utils.file import File
from backend.utils.splitter import Splitter
from backend.utils.huggingface import Embedder as Huggingface_Embedder

def call(file: bytes, filename: str):
    # Get text from file.
    txt = File.get_text(file, filename)
    
    # Make chunks of the text.
    text_chunks = Splitter.get_text_chunks(text=txt)
    
    # Get embedder.
    embedder = Huggingface_Embedder.get(os.getenv("HUGGING_FACE_MODEL_NAME"))
    
    # Store chunks in vector db.
    return PineconeDB.store(
            text_chunks = text_chunks,
            uniq_id = filename.split('.')[0],
            embeddings = embedder
        )
