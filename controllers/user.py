from flask import Blueprint, jsonify, request
from models import db
from models.user import User
from flask_jwt_extended import jwt_required ,get_jwt_identity
import bcrypt

user_bp=Blueprint('user_bp', __name__)

def user_dto(user):
  return {
    'id':user.id,
    'name':user.name,
    'lastname':user.lastname,
    'email':user.email,
    'telephone':user.telephone
  }

def get_current_user():
  id=int(get_jwt_identity())
  user=db.get_or_404(User,id)
  return user

def hash_password(password):
  hashed_pw=bcrypt.hashpw(password, bcrypt.gensalt())
  return hashed_pw

@user_bp.route('/', methods=['GET'])
def get_all():
  users=db.session.execute(db.select(User).order_by(User.id)).scalars()
  dto_list=[user_dto(user) for user in users]
  return jsonify(dto_list)

@user_bp.route('/', methods=['POST'])
def create():
  request_body=request.get_json()
  password=request_body['password']
  hashed_password=hash_password(password.encode('utf-8'))
  if request_body['name'] == '' or request_body['lastname'] == '' or request_body['telephone'] == '' or password == '':
    return jsonify({
      'response':'todos os campos devem ser preenchidos'
    })
  try:
    user=User(
        name=request_body['name'],
        lastname=request_body['lastname'],
        email=request_body['email'],
        telephone='+55'+request_body['telephone'],
        password=hashed_password
    )
    db.session.add(user)
    db.session.commit()
  except Exception as e:
    db.session.rollback()
    print(e)
  return jsonify({
    'response':'usuario cadastrado com sucesso'
  })

@user_bp.route('/<int:id>',methods=['GET'])
@jwt_required()
def get_by_id(id):
    user=db.get_or_404(User,id)
    dto=user_dto(user)
    return jsonify(dto)

@user_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update(id):
  request_body=request.get_json()
  password=request_body['password']
  user=db.get_or_404(User,id)
  hashed_password=hash_password(password.encode('utf-8'))
  try:
    user.name=request_body['name']
    user.lastname=request_body['lastname']
    user.telephone='+55'+request_body['telephone']
    user.password=hashed_password
    db.session.add(user)
    db.session.commit()
  except Exception as e:
    db.session.rollback()
    print(e)
  return jsonify({
      'response':'dados alterados com sucesso'
    })

@user_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete(id):
  try:
    user=db.get_or_404(User,id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({
      'response':'usuario deletado com sucesso'
    })
  except Exception as e:
    db.session.rollback()
    print(e)