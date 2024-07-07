import json
import pdfplumber
from docx import Document
import sys

def parse_pdf_resume(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
    return text

def parse_docx_resume(file_path):
    doc = Document(file_path)
    text = ''
    for para in doc.paragraphs:
        text += para.text + '\n'
    return text

def parse_resume(file_path):
    if file_path.endswith('.pdf'):
        return parse_pdf_resume(file_path)
    elif file_path.endswith('.docx'):
        return parse_docx_resume(file_path)
    else:
        raise ValueError("Unsupported file type")

def resume_to_json(file_path):
    text = parse_resume(file_path)
    resume_json = {
        "content": text
    }
    return json.dumps(resume_json, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <resume_file_path>")
        sys.exit(1)
    
    resume_file_path = sys.argv[1]
    print(resume_to_json(resume_file_path))
