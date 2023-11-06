import psycopg2
from psycopg2 import Error
import config as cf

def crear_tabla(tabla_nombre,create_query):
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
        print(f"Tabla '{tabla_nombre}' creada exitosamente.")

    except (Exception, Error) as error:
        print("Error al crear la tabla:", error)

    finally:
        # Cerrar la conexión y el cursor
        if connection:
            cursor.close()
            connection.close()
            print("Conexión cerrada.")

# Ejemplo de uso
nombre_tabla = input("Ingrese el nombre de la tabla a crear: ")
crear_tabla(nombre_tabla, create_table_query = f'''
            CREATE TABLE {tabla_nombre} (
                id SERIAL PRIMARY KEY,
                nombre VARCHAR(255),
                edad INT
            )
        ''')
