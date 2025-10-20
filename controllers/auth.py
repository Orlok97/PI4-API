from flask import Blueprint, request, jsonify
from models import db
from models.user import User
import bcrypt
from flask_jwt_extended import create_access_token

auth_bp=Blueprint('auth_bp',__name__)

def generate_token(id):
    token = create_access_token(identity=str(id))
    return token

def check_hashed_password(password, hashed_password):
    if bcrypt.checkpw(password, hashed_password):
        return True
    return False

@auth_bp.route('/', methods=['POST'])
def login():
    request_body=request.get_json()
    email=request_body['email']
    password=request_body['password']
    user=db.session.execute(db.select(User).filter_by(email=email)).scalar_one_or_none()
    if user != None:
        if check_hashed_password(password.encode('utf-8'), user.password.encode('utf-8')):
            user_id=user.id
            token=generate_token(user_id)
            return jsonify({
                'response':"usuario autenticado.",
                "access_token":token
            })
        else:
            return jsonify({
                'response':'senha incorreta'
            })
    return jsonify({
        'response':'nenhuma conta associada a esse email foi encontrada.'
    })

   