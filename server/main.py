from fastapi import FastAPI

import config as cf

#uvicorn main:app --reload

# Crea una instancia de FastAPI
app = FastAPI()

# Define una ruta para el endpoint raíz "/"
@app.get("/")
def read_root():
    return {"mensaje": "¡Hola, mundo gzg!"}


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(app, host="0.0.0.0", port=5000)
