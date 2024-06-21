import os.path
from api_actions.process_document import process_document
from api_actions.document_actions_api import (
    get_document_by_id,
    get_all_documents,
    get_documents_by_author,
    get_documents_by_category,
    get_documents_by_title,
    update_document
)
from api_actions.user_api_actions import register_user, login_user, get_user
from init_app import create_app

app = create_app()

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLD = '/tmp'
UPLOAD_FOLDER = os.path.join(APP_ROOT, UPLOAD_FOLD)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# Register Document Endpoints
app.add_url_rule('/process_document', 'process_document', process_document, methods=['POST'])
app.add_url_rule('/documents', 'get_all_documents', get_all_documents, methods=['GET'])
app.add_url_rule('/documents/<int:document_id>', 'get_document_by_id', get_document_by_id, methods=['GET'])
app.add_url_rule('/documents/author/<int:author_id>', 'get_documents_by_author', get_documents_by_author, methods=['GET'])
app.add_url_rule('/documents/category/<int:category_id>', 'get_documents_by_category', get_documents_by_category, methods=['GET'])
app.add_url_rule('/documents/title/<string:title>', 'get_documents_by_title', get_documents_by_title, methods=['GET'])
app.add_url_rule('/documents/<int:document_id>', 'update_document', update_document, methods=['PUT'])

# Register User Endpoints
app.add_url_rule('/register', 'register_user', register_user, methods=['POST'])
app.add_url_rule('/login', 'login_user', login_user, methods=['POST'])
app.add_url_rule('/user/<int:user_id>', 'get_user', get_user, methods=['GET'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)