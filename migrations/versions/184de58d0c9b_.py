"""empty message

Revision ID: 184de58d0c9b
Revises: 8c1bbb9a92fd
Create Date: 2022-01-28 00:43:35.362592

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '184de58d0c9b'
down_revision = '8c1bbb9a92fd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
