"""third

Revision ID: 129f103f0eb4
Revises: 5c24dede7719
Create Date: 2025-02-07 10:49:07.909562

"""
from typing import Sequence, Union

from sqlalchemy.sql import text
from src.app.infra.configs.connection import DBConnectionHandler


# revision identifiers, used by Alembic.
revision: str = '129f103f0eb4'
down_revision: Union[str, None] = '5c24dede7719'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    db_connection_handler = DBConnectionHandler()
    engine = db_connection_handler.get_engine()
    with engine.connect() as conn:
        conn.execute(
            text(
                '''
                    INSERT INTO filmes (titulo, genero, ano)
                    VALUES ('Estou', 'aqui', 777);
                '''
            )
        )
        conn.commit()


def downgrade() -> None:
    db_connection_handler = DBConnectionHandler()
    engine = db_connection_handler.get_engine()
    with engine.connect() as conn:
        conn.execute(
            text(
                '''
                    DELETE FROM filmes
                    WHERE titulo = 'Estou';
                '''
            )
        )
        conn.commit()
