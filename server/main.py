from fastapi import FastAPI

#uvicorn main:app --reload

# Crea una instancia de FastAPI
app = FastAPI()

# Define una ruta para el endpoint raíz "/"
@app.get("/")
def read_root():
    return {"mensaje": "¡Hola, mundo!"}
