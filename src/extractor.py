import pdfplumber

def extract_text_from_pdf(filepath: str) -> str:
    text = ""
    with pdfplumber.open(filepath) as doc:
        for page in doc.pages:
            if page.extract_text():
                text += page.extract_text() + "\n"
    return text
