import json
from Base.Base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Usuario(Base):
    __tablename__ = 'usuarios'

    id_usuario = Column(Integer, primary_key=True)
    nome = Column(String)
    email = Column(String)
    senha = Column(String)

    vendas = relationship("Venda", back_populates="usuario")

    def to_dict(self):
        return {
            'id_usuario': self.id_usuario,
            'nome': self.nome,
            'email': self.email,
            'senha': self.senha
        }

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.to_dict(), indent=4)