import fitz

def extract_resume_text(pdf_bytes):
    """
    Reads a PDF from memory (bytes)
    and returns all extracted text.
    """

    document = fitz.open(stream=pdf_bytes, filetype="pdf")

    resume_text = ""

    for page in document:
        resume_text += page.get_text()

    document.close()

    return resume_text