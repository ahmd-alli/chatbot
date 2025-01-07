import os
from langfuse.decorators import observe
from backend.utils.str import String
from backend.service.google import LLM
from backend.service.pinecone import PineconeDB
from backend.utils.openai import Embedder as Openai_Embedder

@observe()
def call(question: str) -> str:
    # Get embedder.
    embedder = Openai_Embedder.get()

    filename = os.getenv("KNOWLEDGE_FILE_NAME")

    # Get matching chunks from db.
    matching_chunks = PineconeDB.retrieve(question, embedder, filename.split('.')[0])

    # Convert documents list to text.
    txt = String.document_to_str(matching_chunks)

    # Prepare prompt.
    prompt = f"""The document text below is taken from a person's resume. Please read it carefully and answer the below question. Please don't give an answer outside of this document text. Also, format the answer if required.

        Document Text: {txt}
        Question: {question}
    """

    # Get model.
    model = LLM.get()

    # Ask.
    ans = model.generate_content(prompt)
    return  ans.text
