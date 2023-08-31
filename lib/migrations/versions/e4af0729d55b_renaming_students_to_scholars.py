"""Renaming students to scholars

Revision ID: e4af0729d55b
Revises: 791279dd0760
Create Date: 2023-08-31 13:25:02.008407

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4af0729d55b'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')