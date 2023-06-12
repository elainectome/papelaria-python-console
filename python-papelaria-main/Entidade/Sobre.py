from Base.Base import Base
from sqlalchemy import Column, Integer, String

class Sobre(Base):
    __tablename__ = 'sobreProj'

    id_sobre = Column(Integer, primary_key=True)
    sobre = Column(String)