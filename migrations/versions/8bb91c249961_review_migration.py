"""review Migration

Revision ID: 8bb91c249961
Revises: c979e4196d70
Create Date: 2018-07-02 23:29:34.967873

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8bb91c249961'
down_revision = 'c979e4196d70'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reviewadvertisement', sa.Column('advertisement_id', sa.Integer(), nullable=True))
    op.drop_constraint('reviewadvertisement_production_id_fkey', 'reviewadvertisement', type_='foreignkey')
    op.create_foreign_key(None, 'reviewadvertisement', 'advertisement', ['advertisement_id'], ['id'])
    op.drop_column('reviewadvertisement', 'production_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reviewadvertisement', sa.Column('production_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'reviewadvertisement', type_='foreignkey')
    op.create_foreign_key('reviewadvertisement_production_id_fkey', 'reviewadvertisement', 'advertisement', ['production_id'], ['id'])
    op.drop_column('reviewadvertisement', 'advertisement_id')
    # ### end Alembic commands ###