import os
from langchain_openai import ChatOpenAI


class LLM:
    def get(model="gpt-4o"):
        return ChatOpenAI(model=model, openai_api_key=os.getenv("OPENAI_API_KEY"))
