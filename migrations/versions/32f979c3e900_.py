"""empty message

Revision ID: 32f979c3e900
Revises: ba847596c0a9
Create Date: 2024-04-05 09:39:39.489741

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32f979c3e900'
down_revision = 'ba847596c0a9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('plan', schema=None) as batch_op:
        batch_op.add_column(sa.Column('searches_per_day', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('has_notifications_access', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('has_gpt_access', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('plan', schema=None) as batch_op:
        batch_op.drop_column('has_gpt_access')
        batch_op.drop_column('has_notifications_access')
        batch_op.drop_column('searches_per_day')

    # ### end Alembic commands ###