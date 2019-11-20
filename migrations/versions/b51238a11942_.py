"""empty message

Revision ID: b51238a11942
Revises: 1d7a39c4cf61
Create Date: 2019-11-16 20:52:01.616255

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b51238a11942'
down_revision = '1d7a39c4cf61'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        "INSERT INTO topics (name) VALUES \
            ('Soporte tecnico'), \
            ('Seguimiento'), \
            ('Satisfaccion'), \
            ('Confirmacion de entrega'), \
            ('Encuesta')"
    )


def downgrade():
    op.execute("DELETE FROM topics;")
    op.execute("ALTER SEQUENCE topics_id_seq RESTART WITH 1;")
