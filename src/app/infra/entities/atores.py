from src.app.infra.configs.base import Base
from sqlalchemy import Column, BigInteger, String, ForeignKey

class Atores(Base):
    __tablename__ = 'atores'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    titulo_filme = Column(String(50), ForeignKey('filmes.titulo'))

    def __repr__(self):
        return f'Atores: (nome={self.nome}, filme={self.titulo_filme})'
