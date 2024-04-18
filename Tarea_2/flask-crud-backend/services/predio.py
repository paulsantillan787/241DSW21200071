from flask import Blueprint, request, jsonify
from model.predio import Predio
from utils.db import db

predios = Blueprint("predios", __name__)

@predios.route("/predios/v1", methods=["GET"])
def getMensaje():
    result = {}
    result["data"] = "flask-crud-backend"
    return jsonify(result)

@predios.route("/predios/v1/listar", methods=["GET"])
def getPredios():
    result = {}
    predios = Predio.query.all()
    result["data"] = predios
    result["status_code"] = 200
    result["message"] = "Predios listados correctamente"
    return jsonify(result), 200
  
@predios.route("/predios/v1/insert", methods=["POST"])
def insert():
    result = {}
    body = request.get_json()
    id_tipo_predio = body.get("id_tipo_predio")
    descripcion = body.get("descripcion")
    ruc = body.get("ruc")
    telefono = body.get("telefono")
    correo = body.get("correo")
    direccion = body.get("direccion")
    idubigeo = body.get("idubigeo")
    id_persona = body.get("id_persona")
    url_imagen = body.get("url_imagen")
    
    if not id_tipo_predio or not descripcion or not ruc or not telefono or not correo or not direccion or not idubigeo or not id_persona or not url_imagen:
        result["status_code"] = 400
        result["message"] = "Faltan datos"
        return jsonify(result), 400
    
    predio = Predio(id_tipo_predio = id_tipo_predio, descripcion = descripcion, ruc = ruc, telefono = telefono, correo = correo, direccion = direccion, idubigeo = idubigeo, id_persona = id_persona, url_imagen = url_imagen)
    db.session.add(predio)
    db.session.commit()
    
    result["data"] = predio
    result["status_code"] = 201
    result["message"] = "Predio creado correctamente"
    return jsonify(result), 201
  
@predios.route("/predios/v1/update", methods=["POST"])
def update():
    result = {}
    body = request.get_json()
    id_predio = body.get("id_predio")
    id_tipo_predio = body.get("id_tipo_predio")
    descripcion = body.get("descripcion")
    ruc = body.get("ruc")
    telefono = body.get("telefono")
    correo = body.get("correo")
    direccion = body.get("direccion")
    idubigeo = body.get("idubigeo")
    id_persona = body.get("id_persona")
    url_imagen = body.get("url_imagen")
    
    if not id_predio or not id_tipo_predio or not descripcion or not ruc or not telefono or not correo or not direccion or not idubigeo or not id_persona or not url_imagen:
        result["status_code"] = 400
        result["message"] = "Faltan datos"
        return jsonify(result), 400
    
    predio = Predio.query.get(id_predio)
    if not predio:
        result["status_code"] = 404
        result["message"] = "Predio no encontrado"
        return jsonify(result), 404
    
    predio.id_tipo_predio = id_tipo_predio
    predio.descripcion = descripcion
    predio.ruc = ruc
    predio.telefono = telefono
    predio.correo = correo
    predio.direccion = direccion
    predio.idubigeo = idubigeo
    predio.id_persona = id_persona
    predio.url_imagen = url_imagen
    db.session.commit()
    
    result["data"] = predio
    result["status_code"] = 200
    result["message"] = "Predio actualizado correctamente"
    return jsonify(result), 200
  
@predios.route("/predios/v1/delete", methods=["DELETE"])
def delete():
    result = {}
    body = request.get_json()
    id_predio = body.get("id_predio")
    
    if not id_predio:
        result["status_code"] = 400
        result["message"] = "Faltan datos"
        return jsonify(result), 400
    
    predio = Predio.query.get(id_predio)
    if not predio:
        result["status_code"] = 404
        result["message"] = "Predio no encontrado"
        return jsonify(result), 404
    
    db.session.delete(predio)
    db.session.commit()
    
    result["data"] = predio
    result["status_code"] = 200
    result["message"] = "Predio eliminado correctamente"
    return jsonify(result), 200