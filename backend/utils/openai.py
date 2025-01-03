import os
from langchain_openai import OpenAIEmbeddings

class Embedder:
    def get():
        return OpenAIEmbeddings(
            openai_api_key=os.getenv("OPENAI_API_KEY"),
            model=os.getenv("OPENAI_EMBEDDER_NAME")
        )