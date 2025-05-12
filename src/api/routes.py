"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
from sqlalchemy import select
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required


api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@api.route('/test', methods=['GET'])
def testing_api():
    return jsonify({"success":True})

#Siempre POST para Registro o Login
@api.route('/register', methods=['POST'])
def register():
    try:
        #extraemos la info del cuerpo
        data = request.json
        #check email y password
        if not data['email'] or not data['password']:
            raise Exception({"error": 'missing data'})
        #buscamos el email en la base de datos
        stm = select(User).where(User.email == data['email'])
        existing_user = db.session.execute(stm).scalar_one_or_none()
        #verficamos que el email NO este registrado
        if existing_user:
            raise Exception({"error": 'email taken, try logging in'})
        #creamos el nuevo usuario
        new_user = User(
            email=data['email'],
            password=data['password'],
            is_active=True
        )
        #añadimos a bd
        db.session.add(new_user)
        #almacenamos cambios en bd
        db.session.commit()
        #retornamos informacion

        #generar token
        token = create_access_token(identity=str(new_user.id))

        return jsonify({"msg": "register ok", "token": token}), 201
    
    except Exception as e: 
        print(e)
        #si hay error, elimiona cualquier cambio
        db.session.rollback()
        return jsonify({"error": "something went wrong"}), 400


@api.route('/login', methods=['POST'])
def login():
    try:
        #extraemos la info del cuerpo
        data = request.json
        #check email y password
        if not data['email'] or not data['password']:
            raise Exception({"error": 'missing data'})
        #buscamos el email en la base de datos
        stm = select(User).where(User.email == data['email'])
        user = db.session.execute(stm).scalar_one_or_none()
        #verficamos que el email NO este registrado
        if not user:
            raise Exception({"error": 'email not found'})
       
       #verificar email/contraseña
        if (user.password != data['password']):
            raise Exception({"error": 'wrong email/password'})

        
        #generamos token 
        token = create_access_token(identity=str(user.id))

#ejemplo de token
# "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc0NzA0MTk3MCwianRpIjoiM2MwYmZiYjMtYmI3Zi00M2M4LThiZTEtOWJlOWQ0NzU5YTIwIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MywibmJmIjoxNzQ3MDQxOTcwLCJjc3JmIjoiZDYxNTdiODEtZDJiNS00MGY3LTg1ZWYtZDNhM2EzYWViMjg0IiwiZXhwIjoxNzQ3MDQyODcwfQ.s6QSB2vzgELW__3AI75xMnpJ5ZtMhwkL1W-MxMQhepA",eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9


        return jsonify({"msg": "login ok", "token": token}), 200  
    
    except Exception as e: 
        print(e)
        #si hay error, elimiona cualquier cambio
        db.session.rollback()
        return jsonify({"error": "something went wrong"}), 400

#endpoint protegido
@api.route('/private', methods=['GET'])
@jwt_required() # si no se recibe un token, no deja que se acceda
def get_user_inf():
    try:
        #extraer identidad del usuario del token (va a ser el id porque lo definimos asi)
        id = get_jwt_identity()
        
        stm = select(User).where(User.id == id)
        user = db.session.execute(stm).scalar_one_or_none()
        if not user:
            return jsonify({"msg": "what tha hell?"}), 418
        
        return jsonify(user.serialize())
    except Exception as e:
        print(e)
        return jsonify({"error": "something went wrong"})