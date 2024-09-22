"""Changed spelling of Claim.expenseType to lowercase expensetype

Revision ID: 4f924d7a4941
Revises: 5089787e16da
Create Date: 2024-04-01 21:36:06.626075

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f924d7a4941'
down_revision = '5089787e16da'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('claim', schema=None) as batch_op:
        batch_op.add_column(sa.Column('expensetype', sa.String(length=255), nullable=True))
        batch_op.drop_column('expenseType')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('claim', schema=None) as batch_op:
        batch_op.add_column(sa.Column('expenseType', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
        batch_op.drop_column('expensetype')

    # ### end Alembic commands ###
