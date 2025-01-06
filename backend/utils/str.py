class String:
    def document_to_str(input):
        return " ".join([doc.page_content for doc in input])
