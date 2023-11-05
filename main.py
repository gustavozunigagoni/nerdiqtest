import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass
import keyring
import flet as ft


import os 
from dotenv import load_dotenv

from notificaciones import smtp
from seguridad import savepass

# Carga las variables de archivo .env en el entorno
email_remitente = os.getenv("EMAIL_REMITENTE")


#def main(page: ft.Page):
#    t = ft.Text(value="Hola mundo!", color="gree")
#    page.controls.append(t)
#    page.update()

#ft.app(target=main)

if __name__ == "__main__":

    # Prueba de uso de administracion de password
    print(savepass.obtener_contrasena("gmail","gustavo"))
    print(savepass.borrar_contrasena("gmail","gustavo"))



