"""second

Revision ID: 5c24dede7719
Revises: 63d0b7b756f1
Create Date: 2025-02-07 10:35:58.835856

"""
from typing import Sequence, Union

from src.app.infra.repository.filmes_repository import FilmesRepository
from src.app.infra.configs.connection import DBConnectionHandler


# revision identifiers, used by Alembic.
revision: str = '5c24dede7719'
down_revision: Union[str, None] = '63d0b7b756f1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    filmes_repository = FilmesRepository(DBConnectionHandler)
    filmes_repository.insert('Ola', 'Mundo', 123)


def downgrade() -> None:
    filmes_repository = FilmesRepository(DBConnectionHandler)
    filmes_repository.delete('Ola')
