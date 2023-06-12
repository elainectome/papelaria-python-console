from Repositorio.VendaRepositorio import VendaRepositorio
from Entidade.Venda import Venda

class VendaService:
    def __init__(self):
        self.repositorio = VendaRepositorio()
    
    def getAll(self):
        return self.repositorio.getAll()

    def getById(self, id_venda):
        return self.repositorio.getById(id_venda)

    def criarVenda(self, id_usuario, id_produto, quantidade_comprada, data_compra, valor_total):
        venda = Venda(id_usuario=id_usuario, id_produto=id_produto, quantidade_comprada=quantidade_comprada, data_compra=data_compra, valor_total=valor_total)
        self.repositorio.criarVenda(venda)

    def updateVenda(self, id_venda, id_usuario, id_produto, quantidade_comprada, data_compra, valor_total ):
        venda = self.repositorio.getById(id_venda)
        venda.id_usuario = id_usuario
        venda.id_produto = id_produto
        venda.quantidade_comprada = quantidade_comprada
        venda.data_compra = data_compra
        venda.valor_total = valor_total
        self.repositorio.updateVenda(venda)

    def deleteVenda(self, id_venda):
        self.repositorio.deleteVenda(id_venda)