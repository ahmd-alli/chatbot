from langchain.text_splitter import RecursiveCharacterTextSplitter

class Splitter:
    def split(chunk_size: int = 1200, chunk_overlap: int = 200):
        return RecursiveCharacterTextSplitter(
            chunk_size = chunk_size,
            chunk_overlap = chunk_overlap,
            separators = ["\n\n", "\n", r"(?<=\.)", " ", ""]
        )
    
    def get_text_chunks(text: str, chunk_size: int = 1200, chunk_overlap_percentage: int = 20):
        chunk_overlap = int(chunk_size * (chunk_overlap_percentage / 100))
        return Splitter.split(chunk_size, chunk_overlap).split_text(text)
