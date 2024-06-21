from flask import request, jsonify
from model import Document
from datetime import datetime
from init_app import db


def get_all_documents():
    try:
        documents = Document.query.all()
        document_list = [document.to_dict() for document in documents]
        return jsonify(document_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def get_document_by_id(document_id):
    document = Document.query.get_or_404(document_id)
    return jsonify(document.to_dict())


def get_documents_by_author(author_id):
    documents = Document.query.filter_by(author_id=author_id).all()
    return jsonify([doc.to_dict() for doc in documents])


def get_documents_by_category(category_id):
    documents = Document.query.filter_by(category_id=category_id).all()
    return jsonify([doc.to_dict() for doc in documents])


def get_documents_by_title(title):
    documents = Document.query.filter(Document.title.ilike(f'%{title}%')).all()
    return jsonify([doc.to_dict() for doc in documents])


def update_document(document_id):
    document = Document.query.get_or_404(document_id)
    data = request.json
    document.title = data.get('title', document.title)
    document.category_id = data.get('category_id', document.category_id)
    document.last_modified_date = datetime.utcnow()
    db.session.commit()
    return jsonify(document.to_dict())