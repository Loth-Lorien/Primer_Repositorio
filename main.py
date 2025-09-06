from fastapi import FastAPI
from uvicorn import run
app = FastAPI()

@app.get("/inicio")
def inicio():
    return "Bienvenido a la api rest de eventos"

@app.post("/eventos")
async def crear_evento():
    return "Crear un evento"

@app.put("/eventos")
async def Modificar_eventos():
    return "Modificar un evento"
@app.delete("/eventos")
async def Eliminar_eventos():
    return "Eliminar un evento" 
@app.get("/eventos/{idEvento}")
async def optener_eventos(idEvento:int):
    return "optener evento con id: {idEvento}"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app",reload=True,host="127.0.0.1",port=8000)