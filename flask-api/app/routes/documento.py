from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity

from app import db
from app.models import Documento

doc_bp = Blueprint('doc', __name__)


@doc_bp.route('/documento', methods=['GET'])
def get_documentos():
    documentos = Documento.query.all()
    documentos_list = []
    for documento in documentos:
        documentos_list.append({
            'id': documento.id,
            'username': documento.username,
            'titulo': documento.titulo,
            'contenido': documento.contenido
        })
    return jsonify(documentos_list)


@doc_bp.route('/documento', methods=['POST'])
@jwt_required()
def agregar_documento():
    data = request.get_json()
    if not data:
        return jsonify({'message': 'No se ha enviado un documento'}), 400

    user = get_jwt_identity()

    if 'massive' in data:
        for documento in data['massive']:
            doc = Documento(username=user,
                            titulo=documento['titulo'],
                            contenido=documento['contenido'])
            db.session.add(doc)
            db.session.commit()
        return jsonify({'message': 'Documentos creados exitosamente'}), 201
    else:
        if not 'titulo' in data or not 'contenido' in data:
            return jsonify({'message': 'No se ha enviado un documento'}), 400
        doc = Documento(username=user, titulo=data['titulo'],
                        contenido=data['contenido'])
        db.session.add(doc)
        db.session.commit()
        return jsonify({'message': 'Documento creado exitosamente'}), 201
