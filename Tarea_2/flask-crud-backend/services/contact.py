from flask import Blueprint, request, jsonify
from model.contact import Contact
from utils.db import db


# __name__ en blueprint es el nombre del módulo
contacts = Blueprint("contacts", __name__)


# @app.route se usa cuando se require cuando no se tiene un blueprint
@contacts.route("/contacts/v1", methods=["GET"])
def getMensaje():
    result = {}
    result["data"] = "flask-crud-backend"
    return jsonify(result)
  
@contacts.route("/contacts/v1/listar", methods=["GET"])
def getContactos():
    result = {}
    contacts = Contact.query.all()
    result["data"] = contacts
    result["status_code"] = 200
    result["message"] = "Contactos listados correctamente"
    return jsonify(result), 200

@contacts.route("/contacts/v1/insert", methods=["POST"])
def insert():
    result = {}
    body = request.get_json()
    fullname = body.get("fullname")
    email = body.get("email")
    phone = body.get("phone")
    
    if not fullname or not email or not phone:
        result["status_code"] = 400
        result["message"] = "Faltan datos"
        return jsonify(result), 400
    
    contact = Contact(fullname = fullname, email = email, phone = phone)
    db.session.add(contact)
    db.session.commit()
    
    result["data"] = contact
    result["status_code"] = 201
    result["message"] = "Contacto creado correctamente"
    return jsonify(result), 201

@contacts.route("/contacts/v1/update", methods=["POST"])
def update():
    result = {}
    body = request.get_json()
    id = body.get("id")
    fullname = body.get("fullname")
    email = body.get("email")
    phone = body.get("phone")
    
    if not id or not fullname or not email or not phone:
        result["status_code"] = 400
        result["message"] = "Faltan datos"
        return jsonify(result), 400
    
    contact = Contact.query.get(id)
    if not contact:
        result["status_code"] = 404
        result["message"] = "Contacto no encontrado"
        return jsonify(result), 404
    
    contact.fullname = fullname
    contact.email = email
    contact.phone = phone
    db.session.commit()
    
    result["data"] = contact
    result["status_code"] = 200
    result["message"] = "Contacto actualizado correctamente"
    return jsonify(result), 202

@contacts.route("/contacts/v1/delete", methods=["DELETE"])
def delete():
    result = {}
    body = request.get_json()
    id = body.get("id")
    
    if not id:
        result["status_code"] = 400
        result["message"] = "Faltan datos"
        return jsonify(result), 400
    
    contact = Contact.query.get(id)
    if not contact:
        result["status_code"] = 404
        result["message"] = "Contacto no encontrado"
        return jsonify(result), 404
    
    db.session.delete(contact)
    db.session.commit()
    
    result["status_code"] = 200
    result["message"] = "Contacto eliminado correctamente"
    return jsonify(result), 200
    
    
    
