from BancoDados.ConfiguracaoDB import get_db
from Entidade.Sobre import Sobre

class SobreRepositorio:
    def __init__(self):
        self.db = next(get_db())

    def getAll(self):
        return self.db.query(Sobre).all()
    
    def getById(self, id_sobre):
        return self.db.query(Sobre).filter(Sobre.id_sobre == id_sobre).first()
