from sqlalchemy import create_engine, Integer, String, Column
from sqlalchemy.orm import sessionmaker, declarative_base

# Configurações
engine = create_engine('mysql+pymysql://root:root123@localhost:3306/cinema')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Entidades
class Filmes(Base):

    __tablename__ = 'filmes'

    titulo = Column(String(50), primary_key=True)
    genero = Column(String(30), nullable=False)
    ano = Column(Integer, nullable=False)

    def __repr__(self):
        return f'Filme: (titulo={self.titulo} ano={self.ano})'

# SQL

# INSERT
data_insert = Filmes(titulo='Batman', genero='Ação', ano=2008)
session.add(data_insert)
session.commit()

# DELETE
data_delete = session.query(Filmes) \
    .filter(Filmes.titulo == 'Alguma coisa') \
    .first()
session.delete(data_delete)
session.commit()

# UPDATE
session.query(Filmes) \
    .filter(Filmes.genero == 'Drama') \
    .update({Filmes.ano: 2000})

# SELECT
data = session.query(Filmes).all()
print(data)
print(data[0].titulo)

session.close()