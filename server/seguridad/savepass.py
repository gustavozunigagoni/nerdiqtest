import getpass
import keyring

def obtener_contrasena(nombreservicio:str,nombreusuario:str):
    # Intenta obtener la contraseña almacenada en el llavero del sistema
    contraseña = keyring.get_password(nombreservicio, nombreusuario)
    if contraseña is None:
        # Si no se encuentra en el llavero, solicita la contraseña al usuario
        contraseña = getpass.getpass("Introduce tu contraseña de Gmail y presiona Enter: ")
        # Almacena la contraseña en el llavero del sistema de forma segura
        keyring.set_password(nombreservicio, nombreusuario, contraseña)
    return contraseña

def borrar_contrasena(nombreservicio:str,nombreusuario:str):
    try:
        keyring.delete_password(nombreservicio, nombreusuario)
        val = True
    except Exception as e:
        print("Error al tratar de borrar password", str(e))
        val = False
    return val
