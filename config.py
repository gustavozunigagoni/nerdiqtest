import os 
from dotenv import load_dotenv

# Carga las variables del archivo .env en el entorno
load_dotenv()

# Accede a las variables de entorno utilizando os.getenv()
email_server = os.getenv("MAIL_SERVER")
email_main_port = os.getenv("MAIL_PORT")
email_use_tls = os.getenv("MAIL_USE_TLS")
email_username = os.getenv("MAIL_USERNAME")
email_password = os.getenv("MAIL_PASSWORD")
secret_key = os.getenv("SECRET_KEY")
url_site = os.getenv("URL_SITE")
db_pg_host = os.getenv("DB_PG_HOST")
db_pg_database = os.getenv("DB_PG_DATABASE")
db_pg_port = os.getenv("DB_PG_PORT")
db_pg_user = os.getenv("DB_PG_USER")
db_pg_password = os.getenv("DB_PG_PASSWORD")