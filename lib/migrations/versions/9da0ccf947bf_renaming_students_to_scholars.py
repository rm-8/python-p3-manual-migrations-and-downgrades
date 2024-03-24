"""Renaming students to scholars

Revision ID: 9da0ccf947bf
Revises: 791279dd0760
Create Date: 2024-03-24 23:53:34.032048

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9da0ccf947bf'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
