import logging
import os.path
import docx
from PyPDF2 import PdfReader


# Configure logging
logging.basicConfig(level=logging.ERROR)


def read_doc_txt(file_path):
    txt_content = ""
    # Check if file exists
    if not os.path.exists(file_path):
        logging.error("File not found")
        return txt_content
    # Get file extension
    file_ext = os.path.splitext(file_path)[1].lower()
    # Supported file formats
    supported_formats = ['.txt', '.docx', '.pdf']
    if file_ext in supported_formats:
        try:
            if file_ext == '.txt':
                with open(file_path, 'r', encoding='utf-8') as file:
                    txt_content = file.read()

            elif file_ext == '.docx':
                doc = docx.Document(file_path)
                txt_content = '\n'.join([para.text for para in doc.paragraphs])

            elif file_ext == '.pdf':
                reader = PdfReader(file_path)
                txt_content = ''
                for page in reader.pages:
                    txt_content += page.extract_text()
        except Exception as e:
            logging.error(f"Error reading file: {e}")
    else:
        logging.error("Unsupported file format")
    return txt_content


if __name__ == "__main__":
    # example test
    path = './demo_files/Legal.docx'
    content = read_doc_txt(path)
    print(content)


