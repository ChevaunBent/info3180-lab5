"""empty message

Revision ID: 1c237c234265
Revises: 65fce2a93943
Create Date: 2021-03-07 17:24:21.432878

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c237c234265'
down_revision = '65fce2a93943'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profiles', sa.Column('password', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profiles', 'password')
    # ### end Alembic commands ###
