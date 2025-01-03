import os
from backend.service.pinecone import PineconeDB
from backend.utils.file import File
from backend.utils.splitter import Splitter
from backend.utils.openai import Embedder as openai_embedder

def call(file: bytes, filename: str):
    # Get text from file.
    txt = File.get_text(file, filename)
    
    # Make chunks of the text.
    text_chunks = Splitter.get_text_chunks(text=txt)
    
    # Get embedder.
    embedder = openai_embedder.get()
    
    # Store chunks in vector db.
    return PineconeDB.store(
            text_chunks = text_chunks,
            uniq_id = filename.split('.')[0],
            embeddings = embedder
        )
