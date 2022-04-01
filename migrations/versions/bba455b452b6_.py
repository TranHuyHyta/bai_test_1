"""empty message

Revision ID: bba455b452b6
Revises: 0677deee269c
Create Date: 2022-03-31 11:50:38.989186

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bba455b452b6'
down_revision = '0677deee269c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('registered_on', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'registered_on')
    # ### end Alembic commands ###