from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.app.infra.entities.filmes import Filmes
from src.app.infra.repository.filmes_repository import FilmesRepository

class ConnectionHandlerMock:
    def __init__(self):
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(Filmes)],
                    [
                        Filmes(titulo='Alice', genero='Drama', ano=12),
                        Filmes(titulo='Rafael', genero='Drama', ano=12)
                    ]
                ),
                (
                    [
                        mock.call.query(Filmes),
                        mock.call.filter(Filmes.genero=='Drama')
                    ],
                    [Filmes(titulo='Rafael', genero='Drama', ano=12)],
                )
            ]
        )
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

def test_select():
    filmes_repository = FilmesRepository(ConnectionHandlerMock)
    response = filmes_repository.select()
    print()
    print(response)
    assert isinstance(response, list)
    assert len(response) == 2
    assert isinstance(response[0], Filmes)
    assert response[0].titulo == 'Alice'

def test_select_drama_filmes():
    filmes_repository = FilmesRepository(ConnectionHandlerMock)
    response = filmes_repository.select_drama_filmes()
    print()
    print(response)
    assert isinstance(response, Filmes)
    assert response.titulo == 'Rafael'

def test_insert():
    filmes_repository = FilmesRepository(ConnectionHandlerMock)
    response = filmes_repository.insert('Caio', 'Drama', 12)
    print()
    print(response)
    assert isinstance(response, Filmes)
    assert response.titulo == 'Caio'
