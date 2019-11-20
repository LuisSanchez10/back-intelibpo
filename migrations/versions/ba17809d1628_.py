"""empty message

Revision ID: ba17809d1628
Revises: b51238a11942
Create Date: 2019-11-16 21:08:00.878692

"""
from alembic import op
import sqlalchemy as sa
from faker import Faker
import random

# revision identifiers, used by Alembic.
revision = 'ba17809d1628'
down_revision = 'b51238a11942'
branch_labels = None
depends_on = None


def upgrade():
    fake = Faker()
    for i in range(0, 2000): 
        op.execute(
            "INSERT INTO calls (first_name, last_name, call_time, duration_call, topic_id) VALUES \
            ('%s','%s','%s',%i,%i)" % (fake.first_name(), fake.last_name(), str(fake.date_time_this_year()), random.randint(60, 6000), random.randint(1, 5))
        )


def downgrade():
    op.execute("DELETE FROM calls;")
    op.execute("ALTER SEQUENCE calls_id_seq RESTART WITH 1;")
