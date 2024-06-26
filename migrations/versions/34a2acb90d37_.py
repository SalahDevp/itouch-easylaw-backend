"""empty message

Revision ID: 34a2acb90d37
Revises: c665a7793dcb
Create Date: 2024-04-05 10:25:20.632220

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34a2acb90d37'
down_revision = 'c665a7793dcb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('plan', schema=None) as batch_op:
        batch_op.drop_constraint('uq_your_model_name', type_='unique')
        batch_op.create_unique_constraint('uq_plan_name', ['name'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('plan', schema=None) as batch_op:
        batch_op.drop_constraint('uq_plan_name', type_='unique')
        batch_op.create_unique_constraint('uq_your_model_name', ['name'])

    # ### end Alembic commands ###
