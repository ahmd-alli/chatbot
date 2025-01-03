import os
from backend.utils.str import String
from backend.service.llm import LLM
from backend.service.pinecone import PineconeDB
from backend.utils.huggingface import Embedder as Huggingface_Embedder
from backend.utils.openai import Embedder as Openai_Embedder

def call(question :str):
    # Get embedder.
    embedder = Openai_Embedder.get()
    
    filename = os.getenv("KNOWLEDGE_FILE_NAME")
    
    # Get matching chunks from db.
    matching_chunks = PineconeDB.retrieve(question, embedder, filename.split('.')[0])
    
    # Convert documents list to text.
    txt = String.document_to_str(matching_chunks)
    
    # Prepare prompt.
    prompt = """The document text below is taken from a person's resume. Please read it carefully and answer the below question. Please don't give an answer outside of this document text. also, format the answer if required.

        Document Text: {txt}
        Question: {question}
    """.format(txt=txt, question=question)
    
    # Ask LLM.
    llm = LLM.get()
    return llm.invoke(prompt).content 
    
