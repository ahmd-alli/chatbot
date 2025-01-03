from langchain_huggingface import HuggingFaceEmbeddings

class Embedder:
    def get(model_name:str):
        return HuggingFaceEmbeddings(model_name=model_name)