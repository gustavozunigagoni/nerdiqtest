# Mantenimiento de usuarios

from flask import jsonify
import jwt
import datetime

def registro(nombre_usuario,contrasena,secret):
    token = jwt.encode({'usuario': nombre_usuario, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)},secret, algorithm='HS256')
    print(secret)
    return jsonify({'mensaje': 'Usuario registrado exitosamente', 'token': token}), 201



