from BancoDados.ConfiguracaoDB import get_db
from Entidade.Produtos import Produtos

class ProdutosRepositorio:
    def __init__(self):
        self.db = next(get_db())

    def getAll(self):
        return self.db.query(Produtos).all()

    def getById(self, id_produto):
        return self.db.query(Produtos).filter(Produtos.id_produto == id_produto).first()

    def criarProduto(self, produtos):
        self.db.add(produtos)
        self.db.commit()

    def updateProduto(self, produto):
        self.db.merge(produto)
        self.db.commit()

    def deleteProduto(self, id_produto):
        produto = self.db.query(Produtos).filter(Produtos.id_produto == id_produto).first()
        if produto is not None:
            self.db.delete(produto)
            self.db.commit()
