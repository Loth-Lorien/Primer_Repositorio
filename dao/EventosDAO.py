from sqlmodel import Session
from models.EventosModel import vEventos

class EventosDAO:
    def __init__(self, session: Session):
        self.session = session

    def consultar(self):
        lista=self.session.query(vEventos).all()
        return lista



        query = "SELECT * FROM vEventos"
        result = self.session.execute(query)
        eventos = result.fetchall()
        return eventos