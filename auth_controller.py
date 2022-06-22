from crypt import methods
from lib2to3.pgen2 import token
from locale import currency
from flask import Flask, jsonify, request
from app import app, db
from app import User
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from werkzeug.security import check_password_hash
import json
import jwt
import datetime

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    
    if "email" not in data or data["email"] is None:
        return jsonify ({"Error":True, "Message": "email não foi informado"}), 400

    if "password" not in data or data["password"] is None:
        return jsonify ({"Error":True, "Message": "password não foi informado"}), 400
    
    user = User.query.filter_by(email=data["email"]).first()
    if user is None:
        return jsonify ({"Error":True, "Message":"Usuario não existe"})
    
    if check_password_hash and (user.password, data["password"]) and user.password in data == False:
        return jsonify ({"message":"senha incorreta"})

    if check_password_hash and (user.password, data["password"]) == False:
        return jsonify ({"message":"senha incorreta"})

    access_token = create_access_token(identity=user.email)
    refresh_token = create_refresh_token(identity=user.email)
   
   
    return jsonify({"access_token":access_token, "refresh_token":refresh_token, "messsage":"Token de acesso foi gerado"})

@app.route("/me", methods=["GET"])
@jwt_required()
def me():
    current_identity = get_jwt_identity()
    return jsonify ({"message": current_identity, "message":"logado com sucesso!!"}), 200


@app.route("/protected", methods=["GET"])
@jwt_required(optional=True)
def protected():
    current_identity = get_jwt_identity()
    if current_identity:
        return jsonify(logged_in_as=current_identity)
    else:
        return jsonify(logged_in_as="usuário anonimo")
