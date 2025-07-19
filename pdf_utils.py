from PyPDF2 import PdfReader

def extract_text(path: str) -> str:
    """
    Given a PDF file path, returns all its text as one continuous string.
    """
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text() or ""
        text += page_text + "\n"
    return text

def chunk_text(text: str, chunk_size: int = 1000) -> list[str]:
    """
    Splits a long string into a list of substrings, each up to chunk_size chars.
    """
    return [ text[i:i+chunk_size] for i in range(0, len(text), chunk_size) ]
