"""empty message

Revision ID: d6500405f0d2
Revises: df28d0e23bf8
Create Date: 2022-03-30 16:17:31.089157

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6500405f0d2'
down_revision = 'df28d0e23bf8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cart_item',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('cart_id', sa.Integer(), nullable=True),
    sa.Column('productId', sa.String(length=100), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('subtotal_ex_tax', sa.Float(), nullable=True),
    sa.Column('tax_total', sa.Float(), nullable=True),
    sa.Column('total', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['cart_id'], ['cart.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('productId')
    )
    op.drop_table('product')
    op.drop_constraint('cart_cart_id_key', 'cart', type_='unique')
    op.drop_column('cart', 'cart_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cart', sa.Column('cart_id', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
    op.create_unique_constraint('cart_cart_id_key', 'cart', ['cart_id'])
    op.create_table('product',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('price', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='product_pkey')
    )
    op.drop_table('cart_item')
    # ### end Alembic commands ###
