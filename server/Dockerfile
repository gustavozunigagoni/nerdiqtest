# Usamos la imagen oficial de Python desde Docker Hub
FROM python:3.9

# Establecemos el directorio de trabajo en el contenedor
WORKDIR /app

## Pip dependencias
# Actualiza pip
RUN pip install --upgrade pip

# Copiamos el código Python al contenedor (asegúrate de tener tu código en la misma carpeta que el Dockerfile)
COPY . /app

RUN pip install -r /app/requirements.txt

# Instalamos las dependencias del proyecto (si tienes un requirements.txt)
# RUN pip install -r requirements.txt

EXPOSE 5000

# Comando por defecto para ejecutar cuando se inicie el contenedor
CMD ["tail", "-f", "/dev/null"]  # Reemplaza 'tu_archivo.py' por el nombre de tu archivo Python principal
