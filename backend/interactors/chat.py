import os
from backend.utils.str import String
from backend.service.llm import LLM
from backend.service.pinecone import PineconeDB
from backend.utils.huggingface import Embedder as Huggingface_Embedder


def call(question :str):
    # Get embedder.
    embedder = Huggingface_Embedder.get(os.getenv("HUGGING_FACE_MODEL_NAME"))
    
    filename = os.getenv("KNOWLEDGE_FILE_NAME")
    
    # Get matching chunks from db.
    matching_chunks = PineconeDB.retrieve(question, embedder, filename.split('.')[0])
    
    # Convert documents list to text.
    txt = String.document_to_str(matching_chunks)
    
    # Ask LLM.
    return LLM.ask(question=question, context=txt, additional_prompt="")
