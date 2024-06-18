import os
import logging
import PyPDF2
import docx

# Configure logging
logging.basicConfig(level=logging.ERROR)

# Metadata attributes
meta_atts = ['author', 'title', 'date']


def get_meta(file_path):
    if not os.path.exists(file_path):
        return "File not found"

    if not meta_atts:
        return "No metadata available"

    metadata = {}

    file_ext = os.path.splitext(file_path)[1].lower()

    try:
        if file_ext == '.pdf':
            with open(file_path, 'rb') as file:
                reader = PyPDF2.PdfFileReader(file)
                doc_info = reader.getDocumentInfo()
                metadata = {key[1:]: doc_info[key] for key in doc_info}

        elif file_ext == '.docx':
            doc = docx.Document(file_path)
            core_properties = doc.core_properties

            # Safely get metadata fields
            metadata = {
                'author': core_properties.author if core_properties.author else 'Unknown',
                'title': core_properties.title if core_properties.title else 'Untitled',
                'date': core_properties.created if core_properties.created else 'Unknown'
            }

        elif file_ext == '.txt':
            metadata = {
                'author': 'Unknown',
                'title': os.path.basename(file_path),
                'date': 'Unknown'
            }
        else:
            return "Unsupported file format"

    except Exception as e:
        logging.error(f"Error reading file metadata: {e}")
        return "Error reading metadata"

    if metadata:
        return metadata

    return "Uncategorized"


if __name__ == "__main__":
    # Example usage
    doc_path = "./demo_files/Legal.docx"
    meta_data = get_meta(doc_path)
    print(meta_data)

