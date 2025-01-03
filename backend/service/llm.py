from transformers import pipeline

class LLM:
    def ask(question:str, context:str, additional_prompt=""):
        # Create a pipeline.
        p = pipeline("question-answering", model="sentence-transformers/all-MiniLM-L6-v2")
        
        result = p({
            "question": additional_prompt + question,
            "context": context
        })
        
        return result