import json
from Base.Base import Base
from sqlalchemy import Column, Integer, ForeignKey, Date, Float
from sqlalchemy.orm import relationship

class Venda(Base):
    __tablename__ = 'vendas'

    id_venda = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuarios.id_usuario'))
    id_produto = Column(Integer, ForeignKey('produtos.id_produto'))
    quantidade_comprada = Column(Integer)
    data_compra = Column(Date)
    valor_total = Column(Float)

    usuario = relationship("Usuario", back_populates="vendas")
    produtos = relationship("Produtos", back_populates="vendas")

    def to_dict(self):
        return {
            'id_venda': self.id_venda,
            'id_usuario': self.id_usuario,
            'id_produto': self.id_produto,
            'quantidade_comprada': self.quantidade_comprada,
            'data_compra': str(self.data_compra),
            'valor_total': self.valor_total
        }

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.to_dict(), indent=4)