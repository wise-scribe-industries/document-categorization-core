from datetime import datetime
from init_app import db


class DocumentPrint(db.Model):
    __tablename__ = 'documentprint'
    print_id = db.Column(db.Integer, primary_key=True)
    document_id = db.Column(db.Integer, db.ForeignKey('documents.document_id'), nullable=False)
    last_date_print = db.Column(db.DateTime, default=datetime.utcnow)
    document = db.relationship('Document', back_populates='prints')
