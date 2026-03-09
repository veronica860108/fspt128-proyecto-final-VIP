"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_cors import CORS

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200


@api.route('/profesor/registro',methods=['POST'])
def profesor_registro():
 data= request.get_json()
 nombre= request.get_json()
 email= request.get_json()
 contraseña=request.get_json()

 if not nombre or not email or not contraseña:
    return jsonify({"msg":"Rellenar todos los campos para completar el registro"})
 


 @api.route('/profesor/login', methods=['POST'])
 def profesor_login():
    data= request.get_json()
    email= request.get_json()
    contraseña= request.get_json()

    if not email or not contraseña:
     return jsonify({"msg":"El correo o contraseña son requeridos"})
    


@api.route('/estudiante/registro', methods=['POST'])
def estudiante_registro():
  data= request.get_json()
  nombre=request.get_json()
  email=request.get_json()
  contraseña= request.get_json()

  if not nombre or not email or not contraseña:
    return jsonify({"msg":"Rellenar todos los campos para completar el registro"})
  
#faltan endpoints para editar y eliminar alumno

@api.route('/estudiante/login', methods=['POST'])
def estudiante_login():
  data= request.get_json()
  email= request.get_json()
  contraseña= request.get_json()

  if not email or contraseña:
    return jsonify({"msg":"El correo o contraseña son requeridos"})
  









#CRUD DE CALIFICACIONES


# @api.route('/calificaciones/crear',methods=['POST'])
# def calificaciones_crear():
  

# @api.route('/calificaciones/modificar', methods=['PUT'])
# def calificaciones_modificar():

# @api.route('/calificaciones/eliminar', methods=['DELETE'])
# def calificaciones_eliminar():





#CRUD DE MATERIAS

# @api.route('/materias/crear',methods=['POST'])
# def materias_crear():


# @api.route('/materias/editar',methods=['PUT'])
# def materias_modificar():

# @api.route('/materias/eliminar',methods=['DELETE'])
# def materias_eliminar():


#CRUD DE AULAS

# @api.route('/aula/crear',methods=['POST'])
# def aula_crear():


# @api.route('/aula/editar',methods=['POST'])
# def aula_editar():

# @api.route('/aula/eliminar',methods=['DELETE'])
# def aula_eliminar():
