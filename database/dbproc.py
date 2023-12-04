import psycopg2
from psycopg2 import Error
import config as cf

async def dbexec(descripcion,create_query):
    try:
        # Establecer la conexión a la base de datos
        connection = psycopg2.connect(
            user=cf.db_pg_user,
            password=cf.db_pg_password,
            host=cf.db_pg_host,
            port=cf.db_pg_port,
            database=cf.db_pg_database
        )

        # Crear un cursor para ejecutar comandos SQL
        cursor = connection.cursor()

        # Ejecutar el comando SQL
        cursor.execute(create_query)
        connection.commit()
        print(f"{descripcion}'")
        return True, None

    except (Exception, Error) as error:
        print("Error ejecutar proceso:", error)
        return False, error

    finally:
        # Cerrar la conexión y el cursor
        if connection:
            cursor.close()
            connection.close()
            print("Conexión cerrada.")
