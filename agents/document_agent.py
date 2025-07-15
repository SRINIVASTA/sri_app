import textract

def run_document_parser(file):
    try:
        text = textract.process(file).decode("utf-8")
        return text
    except Exception as e:
        return f"Error parsing document: {e}"
