from flask import Blueprint, request, jsonify
import random
import string

from notificaciones import smtp
import config as cf

user = Blueprint('user', __name__)

users = {}

def generate_confirmation_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@user.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Verifica si el email ya está registrado
    if email in users:
        return jsonify({'error': 'Email already registered'}), 400

    # Genera un código de confirmación y almacena el usuario en la base de datos simulada
    confirmation_code = generate_confirmation_code()
    users[email] = {'password': password, 'confirmed': False, 'confirmation_code': confirmation_code}

    # Envia el correo de confirmación
    subject = 'Confirm your email nerdiqtest'
    body = f'''Your confirmation code is: {confirmation_code}
                go to: {cf.url_site}/api/user/confirm/{email}/{confirmation_code}
            '''     
    smtp.send_email(email=cf.email_username,password=cf.email_password,smtp=cf.email_server,port=cf.email_main_port,reciever_emails=["gustavozunigagoni@yahoo.com"],subject=subject,body=body)

    return jsonify({'message': 'Confirmation email sent'}), 200

@user.route('/confirm/<email>/<confirmation_code>', methods=['GET'])
def confirm(email, confirmation_code):
    # Verifica si el email y el código de confirmación coinciden
    if email in users and users[email]['confirmation_code'] == confirmation_code:
        users[email]['confirmed'] = True
        return jsonify({'message': 'Email confirmed successfully'}), 200
    else:
        return jsonify({'error': 'Invalid confirmation code'}), 400


