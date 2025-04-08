"""Initial migration with Hero, Power and HeroPower models

Revision ID: 12fb3e30059b
Revises: 
Create Date: 2025-04-08 03:54:09.373684

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12fb3e30059b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('hero_base')
    op.drop_table('power')
    op.drop_table('hero')
    op.drop_table('hero_power')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hero_power',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('hero_id', sa.INTEGER(), nullable=False),
    sa.Column('power_id', sa.INTEGER(), nullable=False),
    sa.Column('strength', sa.VARCHAR(length=50), nullable=False),
    sa.ForeignKeyConstraint(['hero_id'], ['hero.id'], ),
    sa.ForeignKeyConstraint(['power_id'], ['power.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('hero',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), nullable=False),
    sa.Column('super_name', sa.VARCHAR(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('power',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), nullable=False),
    sa.Column('description', sa.VARCHAR(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('hero_base',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
