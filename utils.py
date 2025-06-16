import PyPDF2

def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        reader = PyPDF2.PdfReader(uploaded_file)
        return "\n".join([page.extract_text() for page in reader.pages])
    elif uploaded_file.type == "text/plain":
        return uploaded_file.read().decode("utf-8")
    return ""
