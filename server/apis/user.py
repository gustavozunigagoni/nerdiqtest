from quart import Blueprint, request, jsonify

import random
import string
import logging

from notificaciones import smtp
import config as cf
from database import userdb
from utils import tokens

# Configurar el logger para guardar el recuento de solicitudes por segundo
logging.basicConfig(filename=cf.log_file, level=logging.INFO)

user = Blueprint('user', __name__)


def generate_confirmation_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

async def register(data):
    data['password']= cf.encriptar_password(data['password'])
    token = await tokens.create_jwt_token(data=data,exp_token_sec=cf.exp_token_register_sec)
    # Envia el correo de confirmación
    subject = 'Confirm your email nerdiqtest'
    body = f'''Your confirmation register 
                go to: {cf.url_site}/api/user/confirm/{data['email']}/{token}
            '''     
    smtp.send_email(email=cf.email_username,password=cf.email_password,smtp=cf.email_server,port=cf.email_main_port,reciever_emails=[data['email']],subject=subject,body=body)
    logging.info(f"Generacion de solicitud de registro para {data['email']}")
    return jsonify({'message': 'Confirmation email sent'}), 200

@user.route('/register', methods=['POST'])
async def register_router():
    data = await request.get_json()
    result = await register(data=data)
    
    return result


async def confirm(token):
    result = await tokens.validate_jwt_token(token)
    if result == None:
        return jsonify({'message': 'Email confirmed Error'}), 401
    else:
        logging.info(f"Confirmacion de registro {result['email']}")
        await userdb.adduser(email=result['email'],nombre=result['nombre'],password=result['password'],confcod=1)
        return jsonify({'message': 'Email confirmed successfully'}), 200


@user.route('/confirm/<email>/<token>', methods=['GET'])
async def confirm_route(email, token):
    return await confirm(token)



