from fastapi import FastAPI

import config as cf

#uvicorn main:app --reload

# Crea una instancia de FastAPI
app = FastAPI()

# Define una ruta para el endpoint raíz "/"
@app.get("/")
def read_root():
    return {"mensaje": "¡Hola, mundo!"}


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(app, host="127.0.0.1", port=8000)
