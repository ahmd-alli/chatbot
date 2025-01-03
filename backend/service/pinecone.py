import os
from pinecone import Pinecone
from langchain_pinecone import Pinecone as PineconeDb

class PineconeDB:
    def store(uniq_id, text_chunks, embeddings, file_name = ''):
        PineconeDb.from_texts(
            texts = text_chunks,
            embedding = embeddings,
            namespace = uniq_id,
            metadatas = [{'id': f"Section {i+1}"} for i in range(len(text_chunks))],
            index_name = os.getenv("PINECONE_INDEX_NAME")
        )
        return uniq_id