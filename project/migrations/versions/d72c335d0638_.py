"""empty message

Revision ID: d72c335d0638
Revises: 750b2a06aca8
Create Date: 2022-10-27 23:45:31.718204

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd72c335d0638'
down_revision = '750b2a06aca8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('point',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image_name', sa.String(), nullable=True),
    sa.Column('latitude_off', sa.Float(), nullable=True),
    sa.Column('longitude_off', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('point')
    # ### end Alembic commands ###