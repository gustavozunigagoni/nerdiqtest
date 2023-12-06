import os 
import hashlib
from pydantic import BaseModel,FilePath,EmailStr

class envconfig(BaseModel):
    email_server: EmailStr = os.getenv("MAIL_SERVER")
    email_main_port: int  = os.getenv("MAIL_PORT")
    email_use_tls: bool = os.getenv("MAIL_USE_TLS")
    email_username: str = os.getenv("MAIL_USERNAME")
    email_password: str = os.getenv("MAIL_PASSWORD")
    secret_key: str = os.getenv("SECRET_KEY")
    url_site: str = os.getenv("URL_SITE")
    log_file: FilePath = os.getenv("LOG_FILE")
    db_pg_host: str = os.getenv("DB_PG_HOST"),
    db_pg_database: str = os.getenv("DB_PG_DATABASE"),
    db_pg_port: str = os.getenv("DB_PG_PORT"),
    db_pg_user: str = os.getenv("DB_PG_USER"),
    db_pg_password: str = os.getenv("DB_PG_PASSWORD"),
    user_admin: str = os.getenv("USER_ADMIN"),
    user_pass: str = os.getenv("USER_PASS"),
    priv_key_path: FilePath = os.getenv("PRIV_KEY_PATH"),
    pub_key_path: FilePath = os.getenv("PUB_KEY_PATH"),
    exp_token_sec: str = os.getenv("EXP_TOKEN_SEC"),
    exp_token_register_sec: str = os.getenv("EXP_TOKEN_REGISTER_SEC"),


oseconf= envconfig()

def encriptar_password(password):
    # Crear un objeto de hash usando SHA-256
    hasher = hashlib.sha256()
    # Codificar el password como bytes y actualizar el hash con esos bytes
    hasher.update(password.encode('utf-8'))
    # Obtener el hash en formato hexadecimal
    password_hash = hasher.hexdigest()
    # Devolver el hash
    return password_hash