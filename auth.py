from flask import Blueprint, request, jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import db, User
from app.ls.jwt_utils import generate_tokens

auth_bp = Blueprint('auth', __name__)
bcrypt = Bcrypt()

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json

    hashed = bcrypt.generate_password_hash(data['password']).decode('utf-8')

    user = User(email=data['email'], password=hashed)
    db.session.add(user)
    db.session.commit()

    return jsonify({"msg": "Registered successfully"})


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()

    if user and bcrypt.check_password_hash(user.password, data['password']):
        access, refresh = generate_tokens(user.id)
        return jsonify(access_token=access, refresh_token=refresh)

    return jsonify({"msg": "Invalid credentials"}), 401


@auth_bp.route('/dashboard', methods=['GET'])
@jwt_required()
def dashboard():
    user_id = get_jwt_identity()
    return jsonify({"msg": f"Welcome User {user_id}"})
