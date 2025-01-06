import os
from backend.utils.str import String
from backend.service.llm import LLM
from backend.service.pinecone import PineconeDB
from backend.utils.openai import Embedder as Openai_Embedder
from langchain.schema.runnable import RunnablePassthrough
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

def call(question: str) -> str:
    # Get embedder.
    embedder = Openai_Embedder.get()

    filename = os.getenv("KNOWLEDGE_FILE_NAME")

    # Get matching chunks from db.
    matching_chunks = PineconeDB.retrieve(question, embedder, filename.split('.')[0])

    # Convert documents list to text.
    txt = String.document_to_str(matching_chunks)

    # Prepare prompt.
    template = """The document text below is taken from a person's resume. Please read it carefully and answer the below question. Please don't give an answer outside of this document text. Also, format the answer if required.

        Document Text: {txt}
        Question: {question}
    """
    prompt = ChatPromptTemplate.from_template(template)

    # Get model.
    model = LLM.get()

    # Instantiate the output parser.
    output_parser = StrOutputParser()

    # Build the chain properly with the components in sequence.
    chain =  prompt | model | output_parser
    
    # Prepare the input for the chain and invoke it.
    return chain.invoke({"txt": txt, "question": question})
