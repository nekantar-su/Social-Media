"""add content column to posts table

Revision ID: 8a3262f27ca4
Revises: e07739c9b97f
Create Date: 2022-04-05 12:57:14.405244

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a3262f27ca4'
down_revision = 'e07739c9b97f'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_column('posts','content')
    pass
