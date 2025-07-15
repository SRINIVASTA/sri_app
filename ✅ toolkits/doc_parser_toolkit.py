import textract

def parse_document(uploaded_file):
    try:
        text = textract.process(uploaded_file).decode("utf-8")
        return text
    except Exception as e:
        return f"Failed to parse document: {e}"
