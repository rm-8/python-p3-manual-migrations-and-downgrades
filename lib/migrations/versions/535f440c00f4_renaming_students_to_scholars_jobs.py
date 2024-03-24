"""Renaming students to scholars jobs 

Revision ID: 535f440c00f4
Revises: 9bce7e70f72b
Create Date: 2024-03-24 23:59:06.374605

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '535f440c00f4'
down_revision = '9bce7e70f72b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')

    


def downgrade() -> None:
    op.rename_table('scholars', 'students')
    
