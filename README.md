# Resume Parser

This repository contains a Python script that reads a resume (in PDF or DOCX format), parses its content, and outputs the result in JSON format.
## Prompt to ChatGPT
- I need you to parse the content of a resume into JSON format. Here is the content of the resume:
- [Paste the content of the resume here]
- Please extract the relevant details like name, contact information, education, work experience, skills, and any other pertinent sections, and format them into JSON.
  
## Features
- Parse resumes in PDF and DOCX formats.
- Output parsed content in a structured JSON format.

## Requirements
- Python 3.x
- Required libraries: `pdfplumber`, `python-docx`

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/resume-parser.git
    cd resume-parser
    ```

2. **Install Required Libraries**:
    ```bash
    pip install pdfplumber python-docx
    ```

## Usage

1. **Prepare Your Resume**: Save your resume as either a PDF or DOCX file.

2. **Run the Script**:
    ```bash
    python resume_parser.py path/to/your/resume.pdf
    # or for DOCX
    python resume_parser.py path/to/your/resume.docx
    ```

### Example
To parse a resume named `example_resume.pdf` located in the current directory:
```bash
python resume_parser.py example_resume.pdf
