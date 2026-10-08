from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.app.infra.configs.base import Base
from src.app.infra.entities.atores import Atores

class Filmes(Base):
    __tablename__ = 'filmes'

    titulo = Column(String(50), primary_key=True)
    genero = Column(String(30), nullable=False)
    ano = Column(Integer, nullable=False)
    atores = relationship('Atores', backref='atores', lazy="subquery")

    def __repr__(self):
        return f'Filme: (titulo={self.titulo} ano={self.ano})'
