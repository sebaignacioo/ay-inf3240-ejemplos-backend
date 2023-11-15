from flask import jsonify, request, Blueprint
from flask_jwt_extended import create_access_token

from app import db, bcrypt
from app.models import Usuario

auth_bp = Blueprint('auth', __name__)

def existe_usuario(username: str):
    return Usuario.query.get(username) is not None


@auth_bp.route('/registro', methods=['POST'])
def registro():
    data = request.get_json()
    if not data or not 'username' in data:
        return jsonify({'message': 'No se ha enviado un username'}), 400
    if not data or not 'email' in data:
        return jsonify({'message': 'No se ha enviado un email'}), 400
    if not data or not 'password' in data:
        return jsonify({'message': 'No se ha enviado un password'}), 400
    if existe_usuario(data['username']):
        return jsonify({'message': 'El username ya existe'}), 400

    hash_pass = bcrypt.generate_password_hash(data['password']).decode('utf-8')

    usuario = Usuario(username=data['username'], email=data['email'],
                      password=hash_pass, rol='usuario')

    db.session.add(usuario)
    db.session.commit()

    return jsonify({'message': 'Usuario creado exitosamente'}), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or not 'username' in data:
        return jsonify({'message': 'No se ha enviado un username'}), 400
    if not data or not 'password' in data:
        return jsonify({'message': 'No se ha enviado un password'}), 400

    username = request.json['username']
    password = request.json['password']

    usuario = Usuario.query.get(username)
    if usuario and bcrypt.check_password_hash(usuario.password, password):
        access_token = create_access_token(identity=username)
        return jsonify({'access_token': access_token}), 200
    return jsonify({'message': 'Usuario o password incorrecto'}), 401
