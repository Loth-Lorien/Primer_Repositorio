from sqlmodel import SQLModel,Field
from datetime import date

class vEventos(SQLModel, table=True):
    idEvento: int = Field(primary_key=True)
    nombre: str
    cantidadParticipantes: int
    fechaInicio: date
    fechaFin: date
    estatus: str
    descripcion: str
    tipo_evento:str
    departamento:str