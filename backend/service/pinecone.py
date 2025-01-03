import os
from pinecone import Pinecone
from langchain_pinecone import Pinecone as PineconeDb, PineconeVectorStore

class PineconeDB:
    def get():
        return Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

    def store(uniq_id, text_chunks, embeddings, file_name = ''):
        PineconeDb.from_texts(
            texts = text_chunks,
            embedding = embeddings,
            namespace = uniq_id,
            metadatas = [{'id': f"Section {i+1}"} for i in range(len(text_chunks))],
            index_name = [os.getenv("PINECONE_INDEX_NAME")]
        )
        return uniq_id

    def get_index():
        return PineconeDB.get().Index(os.getenv("PINECONE_INDEX_NAME"))

    def retrieve(input,embedder,uniq_id):
        # Get pinecone index.
        index = PineconeDB.get_index()

        # Create a retriever.
        vector_store = PineconeVectorStore(
            index=index,
            embedding=embedder,
            namespace=uniq_id,
        )
        retriever = vector_store.as_retriever(
            search_type="similarity_score_threshold",
            search_kwargs={'score_threshold': 0.7}
        )

        # Retrieve matching chunks.
        matching_chunks = retriever.invoke(input)

        return matching_chunks