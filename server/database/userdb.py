# Mantenimiento de usuarios

from database import dbproc
import server.config as cf

async def adduser(email,nombre,password,confcod):
    script= f"""
INSERT INTO public.users(
	email, nombre, estado, rol, password,confcod)
	VALUES ('{email}', '{nombre}', 2, 0, '{cf.encriptar_password(password)}','{confcod}');
"""
    await dbproc.dbexec("Adicion de registro de nuevo usuario",script)
    