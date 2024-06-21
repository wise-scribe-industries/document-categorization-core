from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from init_app import db
from model import User
import uuid


def register_user():
    data = request.json
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({"error": "Username and password required"}), 400

    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(
        public_id=str(uuid.uuid4()),
        username=data['username'],
        password=hashed_password
    )
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201


def login_user():
    data = request.json
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({"error": "Username and password required"}), 400

    user = User.query.filter_by(username=data['username']).first()
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({"error": "Invalid username or password"}), 401

    return jsonify({"message": "Login successful"}), 200


def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify({
        'public_id': user.public_id,
        'username': user.username,
        'registered_on': user.registered_on
    })
