from datetime import datetime
from init_app import db


class DocumentAccess(db.Model):
    __tablename__ = 'documentaccess'
    access_id = db.Column(db.Integer, primary_key=True)
    document_id = db.Column(db.Integer, db.ForeignKey('documents.document_id'), nullable=False)
    last_access_date = db.Column(db.DateTime, default=datetime.utcnow)
    document = db.relationship('Document', back_populates='accesses')
