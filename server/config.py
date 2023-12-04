import os 
import hashlib

# Accede a las variables de entorno utilizando os.getenv()
email_server = os.getenv("MAIL_SERVER")
email_main_port = os.getenv("MAIL_PORT")
email_use_tls = os.getenv("MAIL_USE_TLS")
email_username = os.getenv("MAIL_USERNAME")
email_password = os.getenv("MAIL_PASSWORD")
secret_key = os.getenv("SECRET_KEY")
url_site = os.getenv("URL_SITE")
log_file = os.getenv("LOG_FILE")
db_pg_host = os.getenv("DB_PG_HOST")
db_pg_database = os.getenv("DB_PG_DATABASE")
db_pg_port = os.getenv("DB_PG_PORT")
db_pg_user = os.getenv("DB_PG_USER")
db_pg_password = os.getenv("DB_PG_PASSWORD")
user_admin = os.getenv("USER_ADMIN")
user_pass = os.getenv("USER_PASS")
priv_key_path = os.getenv("PRIV_KEY_PATH")
pub_key_path = os.getenv("PUB_KEY_PATH")
exp_token_sec = os.getenv("EXP_TOKEN_SEC")
exp_token_register_sec = os.getenv("EXP_TOKEN_REGISTER_SEC")

def encriptar_password(password):
    # Crear un objeto de hash usando SHA-256
    hasher = hashlib.sha256()
    # Codificar el password como bytes y actualizar el hash con esos bytes
    hasher.update(password.encode('utf-8'))
    # Obtener el hash en formato hexadecimal
    password_hash = hasher.hexdigest()
    # Devolver el hash
    return password_hash