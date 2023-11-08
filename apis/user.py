from quart import Blueprint, request, jsonify

import random
import string

from notificaciones import smtp
import config as cf
from database import userdb
from utils import tokens

user = Blueprint('user', __name__)


def generate_confirmation_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

async def register(data):
    print(data)
    data['password']= cf.encriptar_password(data['password'])
    token = await tokens.create_jwt_token(data=data,exp_token_sec=cf.exp_token_register_sec)
    print(token)

    print(await tokens.validate_jwt_token(token))
    
    # Envia el correo de confirmación
    subject = 'Confirm your email nerdiqtest'
    body = f'''Your confirmation register 
                go to: {cf.url_site}/api/user/confirm/{data['email']}/{token}
            '''     
    smtp.send_email(email=cf.email_username,password=cf.email_password,smtp=cf.email_server,port=cf.email_main_port,reciever_emails=[data['email']],subject=subject,body=body)

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
        print(result)
        await userdb.adduser(email=result['email'],nombre=result['nombre'],password=result['password'],confcod=1)
        return jsonify({'message': 'Email confirmed successfully'}), 200


@user.route('/confirm/<email>/<token>', methods=['GET'])
async def confirm_route(email, token):
    return await confirm(token)



