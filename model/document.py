from datetime import datetime
from init_app import db


class Document(db.Model):
    __tablename__ = 'documents'
    document_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    path = db.Column(db.String(255), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.author_id'), nullable=False)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow)
    last_modified_date = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.category_id'), nullable=False)
    author = db.relationship('Author', back_populates='documents')
    category = db.relationship('Category', back_populates='documents')
    prints = db.relationship('DocumentPrint', back_populates='document', cascade='all, delete-orphan')
    accesses = db.relationship('DocumentAccess', back_populates='document', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'document_id': self.document_id,
            'title': self.title,
            'path': self.path,
            'author_id': self.author_id,
            'creation_date': self.creation_date.isoformat() if self.creation_date else None,
            'last_modified_date': self.last_modified_date.isoformat() if self.last_modified_date else None,
            'category_id': self.category_id
        }