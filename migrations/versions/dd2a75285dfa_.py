"""empty message

Revision ID: dd2a75285dfa
Revises: 
Create Date: 2024-08-21 12:47:35.406832

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd2a75285dfa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('persona',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombres', sa.String(length=50), nullable=True),
    sa.Column('apellidos', sa.String(length=50), nullable=True),
    sa.Column('edad', sa.Integer(), nullable=True),
    sa.Column('activo', sa.Boolean(), nullable=True),
    sa.Column('fecha_nacimiento', sa.Date(), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('persona')
    # ### end Alembic commands ###
