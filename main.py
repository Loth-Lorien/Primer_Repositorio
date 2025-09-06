
from fastapi import FastAPI, Request
from uvicorn import run
from dao.database import Conexion
from dao.EventosDAO import EventosDAO
from models.EventosModel import vEventos

app = FastAPI()
@app.on_event("startup")
async def startup_event():
    conexion = Conexion()
    session = conexion.getSession()
    app.session = session
    print("Conexión exitosa a la base de datos")

@app.get("/")
async def inicio():
    return "Bienvenido a la API REST de EVENTOS"

@app.post("/eventos")
async def crearEvento():
    return {"mensaje":"Creando un evento"}

@app.put("/eventos")
async def modificarEvento():
    return {"mensaje":"Editando un evento"}

@app.get("/eventos",response_model=list[vEventos],tags=["Eventos"],summary="Consulta de eventos")
async def consultarEventos(request : Request)->list[vEventos]:
    eDAO=EventosDAO(request.app.session)
    return eDAO.consultar()

@app.get("/eventos/{idEvento}")
async def consultaIndividual(idEvento:int):
    return {"mensaje":f'Consultando el evento con id:{idEvento}'}
@app.delete("/eventos")
async def eliminarEvento():
    return {"mensaje":"Eliminando un evento"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app",reload=True,host="127.0.0.1",port=8000)