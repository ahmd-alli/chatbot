import os
import google.generativeai as genai


class LLM:
    def get(model_name="gemini-1.5-flash"):
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        return genai.GenerativeModel(model_name)
