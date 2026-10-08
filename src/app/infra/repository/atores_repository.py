from src.app.infra.configs.connection import DBConnectionHandler
from src.app.infra.entities.atores import Atores
from src.app.infra.entities.filmes import Filmes

class AtoresRepository:

    def __init__(self, connection_handler: type[DBConnectionHandler]):
        self.__connection_handler = connection_handler

    def select(self):
        with self.__connection_handler() as db:
            data = db.session \
                .query(Atores) \
                .join(Filmes, Atores.titulo_filme == Filmes.titulo) \
                .with_entities(
                    Atores.nome,
                    Filmes.genero,
                    Filmes.titulo
                ) \
                .all()
            return data
