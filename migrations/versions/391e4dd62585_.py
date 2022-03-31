"""empty message

Revision ID: 391e4dd62585
Revises: 5e0c8f35783a
Create Date: 2022-03-30 14:11:27.105241

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '391e4dd62585'
down_revision = '5e0c8f35783a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cart', sa.Column('productId', sa.String(length=100), nullable=True))
    op.drop_constraint('cart_product_id_key', 'cart', type_='unique')
    op.create_unique_constraint(None, 'cart', ['productId'])
    op.drop_column('cart', 'product_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cart', sa.Column('product_id', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'cart', type_='unique')
    op.create_unique_constraint('cart_product_id_key', 'cart', ['product_id'])
    op.drop_column('cart', 'productId')
    # ### end Alembic commands ###
