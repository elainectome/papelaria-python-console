import json
from Base.Base import Base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

class Produtos(Base):
    __tablename__ = 'produtos'

    id_produto = Column(Integer, primary_key=True)
    nome = Column(String)
    preco_venda = Column(Float)
    preco_compra = Column(Float)
    grupo = Column(String)
    quantidade_em_estoque = Column(Integer)

    vendas = relationship("Venda", back_populates="produtos")

    def to_dict(self):
        return {
            'id_produto': self.id_produto,
            'nome': self.nome,
            'preco_venda': self.preco_venda,
            'preco_compra': self.preco_compra,
            'grupo': self.grupo,
            'quantidade_em_estoque': self.quantidade_em_estoque
        }

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.to_dict(), indent=4)