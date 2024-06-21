import os
import logging
import PyPDF2
import docx


def get_meta(file):
    meta_atts = ['author', 'title', 'date', 'modify_date']  # Add any necessary metadata attributes

    if not meta_atts:
        return "No metadata available"

    metadata = {}

    # Determine the file extension
    file_ext = os.path.splitext(file.filename)[1].lower()

    try:
        if file_ext == '.pdf':
            # Handle PDF files
            file.seek(0)  # Move to the beginning of the file
            reader = PyPDF2.PdfFileReader(file)
            doc_info = reader.getDocumentInfo()
            metadata = {key[1:]: doc_info[key] for key in doc_info}

        elif file_ext == '.docx':
            # Handle DOCX files
            file.seek(0)  # Move to the beginning of the file
            doc = docx.Document(file)
            core_properties = doc.core_properties

            # Safely get metadata fields
            metadata = {
                'author': core_properties.author if core_properties.author else 'Unknown',
                'title': core_properties.title if core_properties.title else 'Untitled',
                'date': core_properties.created if core_properties.created else 'Unknown',
                'modify_date': core_properties.modified if core_properties.modified else 'unknown'
            }

        elif file_ext == '.txt':
            # Handle TXT files
            metadata = {
                'author': 'Unknown',
                'title': file.filename,
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
    with open("../demo_files/Legal.docx", "rb") as file:
        meta_data = get_meta(file)
        print(meta_data)
