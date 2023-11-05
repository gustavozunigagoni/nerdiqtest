import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviar_correo(destinatario, asunto, mensaje, remitente):
    contraseña = obtener_contraseña()

    # Configuración del servidor SMTP de Gmail
    servidor_smtp = "smtp.gmail.com"
    puerto = 587

    # Crear el objeto del mensaje
    msg = MIMEMultipart()
    msg['From'] = remitente
    msg['To'] = destinatario
    msg['Subject'] = asunto

    # Agregar el cuerpo del mensaje
    msg.attach(MIMEText(mensaje, 'plain'))

    try:
        # Iniciar sesión en el servidor SMTP de Gmail
        servidor = smtplib.SMTP(servidor_smtp, puerto)
        servidor.starttls()  # Habilitar cifrado TLS
        servidor.login(remitente, contraseña)  # Iniciar sesión en la cuenta de Gmail

        # Enviar el mensaje
        servidor.sendmail(remitente, destinatario, msg.as_string())

        # Cerrar la conexión con el servidor SMTP
        servidor.quit()

        print("Correo electrónico enviado correctamente.")
    except Exception as e:
        print("Error al enviar el correo electrónico:", str(e))

if __name__ == "__main__":
    # Ejemplo de uso
    destinatario = input("Introduce la dirección de correo del destinatario: ")
    asunto = input("Introduce el asunto del correo: ")
    mensaje = input("Introduce el cuerpo del mensaje del correo electrónico: ")
    remitente = input("Introduce tu dirección de correo: ")

    enviar_correo(destinatario, asunto, mensaje, remitente)
