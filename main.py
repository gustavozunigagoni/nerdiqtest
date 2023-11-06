import flet as ft
import Qmail
from flask import Flask, request, jsonify

import os 
from dotenv import load_dotenv

from notificaciones import smtp
from seguridad import savepass
from apis import user

# Carga las variables del archivo .env en el entorno
load_dotenv()

# Accede a las variables de entorno utilizando os.getenv()
email_smtp_remitente = os.getenv("EMAIL_SMTP_REMITENTE")
email_smtp_password = os.getenv("EMAIL_SMTP_PASSWORD")
email_smtp_server = os.getenv("EMAIL_SMTP_SERVER")
email_smtp_port = os.getenv("EMAIL_SMTP_PORT")
secret_key = os.getenv("SECRET_KEY")


#def main(page: ft.Page):
#    t = ft.Text(value="Hola mundo!", color="gree")
#    page.controls.append(t)
#    page.update()

#ft.app(target=main)

# Codigo para inicializar la aplicacion de Flask y rutas

app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key

@app.route('/')
def index():
    return 'Hola, mundo!'

#ruta de registro de nuevo usuario
@app.route('/crearusuario',methods=['POST'])
def registro_route():
    datos_usuario = request.get_json()
    nombre_usuario = datos_usuario.get('nombre')
    contrasena = datos_usuario.get('contrasena')
    print(nombre_usuario)
    print("******")
    # Llama la funcion registro() 
    resultado = user.registro(nombre_usuario,contrasena,app.config['SECRET_KEY'])

    return resultado






if __name__ == "__main__":

    # Prueba de uso de administracion de password
    #savepass.borrar_contrasena("gmail","gustavo")
    
    # Prueba de funcionamiento de modulo de smtp
    #smtp.send_email(email=email_smtp_remitente,password=email_smtp_password,smtp=email_smtp_server,port=email_smtp_port,reciever_emails=["gustavozunigagoni@yahoo.com"],subject="Correo de prueba Gustavo 3",txt="Correo de pruebas 3")

    app.run(debug=True)