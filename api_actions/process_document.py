# api_action/document_actions.py

from flask import request, jsonify
from init_app import db
from model import Document, Category, Author
from actions.read_doc_txt import read_doc_txt
from actions.get_cate_by_key import get_cate_by_key
from actions.get_meta import get_meta
import os
import uuid
from werkzeug.utils import secure_filename


def process_document():
    try:
        if 'document' not in request.files:
            return jsonify({"error": "No file part in the request"}), 400

        file = request.files['document']

        # If the user does not select a file, the browser submits an empty part without a filename.
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400

        if file:
            # use secure filename to sanitize the filename
            original_filename = secure_filename(file.filename)
            # Generate a unique filename using UUID
            unique_filename = f"{uuid.uuid4()}_{original_filename}"

            # construct the file path to save the file
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)

            # Save the file
            file.save(file_path)

            document_text = read_doc_txt(file_path)
            category_name = get_cate_by_key(document_text)
            metadata = get_meta(file)

            title = metadata.get('title')
            author_name = metadata.get('author')
            creation_date = metadata.get('date')
            modify_date = metadata.get('modify_date')
            category = Category.query.filter_by(category_name=category_name).first()
            if not category:
                category = Category(category_name=category_name)
                db.session.add(category)

            author = Author.query.filter_by(name=author_name).first()
            if not author:
                author = Author(name=author_name)
                db.session.add(author)

            document = Document(title=title, path=file_path, author=author, category=category,
                                creation_date=creation_date, last_modified_date=modify_date)
            db.session.add(document)
            db.session.commit()

            return jsonify({"message": "Document processed and data saved.", "document_id": document.document_id})
        else:
            return jsonify({"message": "No document provided."}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500
