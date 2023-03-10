"""New Migration

Revision ID: 815bf7462ac8
Revises: d28c51528630
Create Date: 2023-01-14 16:28:53.568628

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '815bf7462ac8'
down_revision = 'd28c51528630'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_code', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('cart_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cart_id'], ['cart.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['product_code'], ['product.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_constraint('product_cart_id_fkey', 'product', type_='foreignkey')
    op.drop_column('product', 'cart_id')
    op.drop_column('product', 'product_code')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('product_code', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('product', sa.Column('cart_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('product_cart_id_fkey', 'product', 'cart', ['cart_id'], ['id'], ondelete='CASCADE')
    op.drop_table('products')
    # ### end Alembic commands ###
