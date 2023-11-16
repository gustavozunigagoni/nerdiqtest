import flet as ft
from quart import Quart

import server.config as cf
from apis.user import user
from apis.root import root

# Codigo para inicializar la aplicacion de Flask y rutas

app = Quart(__name__)

app.config['SECRET_KEY'] = cf.secret_key

# Regristra blueprint del mantenimiento de usuario
app.register_blueprint(user,url_prefix='/api/user')
app.register_blueprint(root)


if __name__ == "__main__":

    # Prueba de uso de administracion de password
    #savepass.borrar_contrasena("gmail","gustavo")
    
    # Prueba de funcionamiento de modulo de smtp
    #smtp.send_email(email=cf.email_username,password=cf.email_password,smtp=cf.email_server,port=cf.email_main_port,reciever_emails=["gustavozunigagoni@yahoo.com"],subject="Correo de prueba Gustavo 4",txt="Correo de pruebas 4")
    
    resultado = app.run(debug=True,host='0.0.0.0',port=5000)


