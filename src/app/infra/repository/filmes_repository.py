from sqlalchemy.orm.exc import NoResultFound
from src.app.infra.configs.connection import DBConnectionHandler
from src.app.infra.entities.filmes import Filmes

class FilmesRepository:

    def __init__(self, connection_handler: type[DBConnectionHandler]):
        self.__connection_handler = connection_handler

    def select(self) -> list:
        with self.__connection_handler() as db:
            try:
                data = db.session.query(Filmes).all()
                return data
            except Exception as exception:
                db.session.rollback()
                raise exception

    def select_drama_filmes(self) -> list:
        with self.__connection_handler() as db:
            try:
                data = db.session.query(Filmes) \
                    .filter(Filmes.genero == 'Drama') \
                    .one()
                return data
            except NoResultFound:
                return None
            except Exception as exception:
                db.session.rollback()
                raise exception

    def insert(self, titulo: str, genero: str, ano: int) -> None:
        with self.__connection_handler() as db:
            try:
                new_filme = Filmes(titulo=titulo, genero=genero, ano=ano)
                db.session.add(new_filme)
                db.session.commit()
                return new_filme
            except Exception as exception:
                db.session.rollback()
                raise exception

    def delete(self, titulo: str) -> None:
        with self.__connection_handler() as db:
            try:
                db.session.query(Filmes) \
                    .filter(Filmes.titulo == titulo) \
                    .delete()
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def update(self, genero: str, ano: int) -> None:
        with self.__connection_handler() as db:
            try:
                db.session.query(Filmes) \
                    .filter(Filmes.genero == genero) \
                    .update({Filmes.ano: ano})
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception
