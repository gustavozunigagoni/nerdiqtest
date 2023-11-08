from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

# Generar un par de claves RSA
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Obtener la clave pública en formato PEM
public_key_pem = private_key.public_key().public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Obtener la clave privada en formato PEM y sin cifrado (NoEncryption)
private_key_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)

# Guardar la clave pública en un archivo PEM
with open('public_key.pem', 'wb') as public_key_file:
    public_key_file.write(public_key_pem)

# Guardar la clave privada en un archivo PEM
with open('private_key.pem', 'wb') as private_key_file:
    private_key_file.write(private_key_pem)

print("Claves generadas y guardadas en public_key.pem y private_key.pem")
