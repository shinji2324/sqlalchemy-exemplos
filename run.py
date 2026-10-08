from src.app.infra.configs.connection import DBConnectionHandler
from src.app.infra.repository.atores_repository import AtoresRepository
from src.app.infra.repository.filmes_repository import FilmesRepository

def main():
    repo = AtoresRepository(DBConnectionHandler)
    data = repo.select()
    print(data)

    repo2 = FilmesRepository(DBConnectionHandler)
    data2 = repo2.select()
    print(data2)


if __name__ == '__main__':
    main()
