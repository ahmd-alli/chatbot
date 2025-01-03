import PyPDF2
from io import BytesIO

class File:
    def get_text(file:bytes, filename:str):
        # Initialize the text content.
        text = ""
        
        try:
            if filename.endswith(".pdf"):
                # Convert bytes to BytesIO.
                pdf = BytesIO(file)
                
                # Get reader.
                r = PyPDF2.PdfReader(pdf)
                
                # Loop through all pages to extract text.
                for page_num in range(len(r.pages)):
                    page = r.pages[page_num]
                    text += page.extract_text()
                
                return text
            
            else:
                return "Unsupported file type."
        
        except Exception as e:
            return f"An error occurred: {str(e)}"
