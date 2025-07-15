import textract

def run_document_parser(uploaded_file):
    try:
        # Read raw bytes from the uploaded file
        content = uploaded_file.read()
        text = textract.process(uploaded_file.name, input_data=content).decode("utf-8")
        return text
    except Exception as e:
        return f"Error parsing document: {e}"
