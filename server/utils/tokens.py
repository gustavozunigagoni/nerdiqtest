# Funsiones para la generacion y validacion de token

import jwt
import datetime
from cryptography.hazmat.primitives import serialization
import server.config as cf

# Funcion para crear un token JWT usando un certificado de clave privada
async def create_jwt_token(data,exp_token_sec):
    with open(cf.priv_key_path, 'rb') as private_key_file:
        private_key = serialization.load_pem_private_key(private_key_file.read(),password=None)

    exp_time = datetime.datetime.utcnow() + datetime.timedelta(seconds=exp_token_sec)
    data['exp'] = exp_time

    #firmar el token usando la clave privada
    token = jwt.encode(data,private_key,algorithm='RS256')
    return token

# Funcion para validar un token JWT usando un certicado de clave publica
async def validate_jwt_token(token):
    with open(cf.pub_key_path, 'rb') as public_key_file:
        public_key = serialization.load_pem_public_key(public_key_file.read())

        try:
            # Decodificar y validar el token usando la clave publica
            decoded_data = jwt.decode(token,public_key,algorithms='RS256')
            return decoded_data
        except jwt.ExpiredSignatureError:
            print("Error: El token ha expirado")
            return None
        except jwt.InvalidTokenError:
            print("Error: Token no valido")
            return None