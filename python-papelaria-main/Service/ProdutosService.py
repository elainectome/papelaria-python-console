from Repositorio.ProdutosRepositorio import ProdutosRepositorio
from Entidade.Produtos import Produtos

class ProdutosService:
    def __init__(self):
        self.repositorio = ProdutosRepositorio()
    
    def getAll(self):
        produtos = self.repositorio.getAll()
        return produtos

    def getById(self, idProduto):
        return self.repositorio.getById(idProduto)

    def criarProduto(self, nome, preco_venda, preco_compra, grupo, quantidade_em_estoque):
        produto = Produtos(nome=nome, preco_venda=preco_venda, preco_compra=preco_compra, grupo=grupo, quantidade_em_estoque=quantidade_em_estoque)
        self.repositorio.criarProduto(produto)

    def updateProduto(self, id_produto, nome, preco_venda, preco_compra, grupo, quantidade_em_estoque):
        produto = self.repositorio.getById(id_produto)
        produto.nome = nome
        produto.preco_venda = preco_venda
        produto.preco_compra = preco_compra
        produto.grupo = grupo
        produto.quantidade_em_estoque = quantidade_em_estoque
        self.repositorio.updateProduto(produto)

    def deleteProduto(self, idProduto):
        self.repositorio.deleteProduto(idProduto)