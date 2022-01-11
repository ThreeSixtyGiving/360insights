"""empty message

Revision ID: 320bf2022418
Revises: c93d17410aaa
Create Date: 2022-01-11 11:00:58.113578

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '320bf2022418'
down_revision = 'c93d17410aaa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('grant', sa.Column('insights_org_id_int', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('grant', 'insights_org_id_int')
    # ### end Alembic commands ###
