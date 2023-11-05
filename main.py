import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass
import keyring
import flet as ft

def main(page: ft.Page):
    t = ft.Text(value="Hola mundo!", color="gree")
    page.controls.append(t)
    page.update()

ft.app(target=main)


