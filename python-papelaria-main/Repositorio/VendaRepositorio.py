from BancoDados.ConfiguracaoDB import get_db
from Entidade.Venda import Venda

class VendaRepositorio:
    def __init__(self):
        self.db = next(get_db())
    
    def getAll(self):
        return self.db.query(Venda).all()

    def getById(self, id_venda):
        return self.db.query(Venda).filter(Venda.id_venda == id_venda).first()

    def criarVenda(self, venda):
        self.db.add(venda)
        self.db.commit()

    def updateVenda(self, venda):
        self.db.merge(venda)
        self.db.commit()

    def deleteVenda(self, id_venda):
        venda = self.db.query(Venda).filter(Venda.id_venda == id_venda).first()
        if venda is not None:
            self.db.delete(venda)
            self.db.commit()
