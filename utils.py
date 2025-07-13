import fitz  # PyMuPDF

def extract_text_from_pdf(uploaded_file):
    text = ""
    try:
        # Rewind file stream if needed
        uploaded_file.seek(0)
        with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
            for page_num, page in enumerate(doc):
                page_text = page.get_text()
                text += f"\n\n[Page {page_num + 1}]\n{page_text}"
    except Exception as e:
        text = f"❌ Error reading PDF: {e}"
    return text.strip()