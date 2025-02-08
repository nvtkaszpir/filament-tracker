"""Initial creation

Revision ID: 0c701aa35f43
Revises: 
Create Date: 2025-01-26 20:35:48.360231

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c701aa35f43'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('filament_roll',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('maker', sa.String(length=100), nullable=False),
    sa.Column('color', sa.String(length=50), nullable=False),
    sa.Column('total_weight', sa.Float(), nullable=False),
    sa.Column('remaining_weight', sa.Float(), nullable=False),
    sa.Column('in_use', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('temp_print_job',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('project_name', sa.String(length=255), nullable=False),
    sa.Column('weight_used', sa.Float(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('print_job',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('filament_id', sa.Integer(), nullable=False),
    sa.Column('weight_used', sa.Float(), nullable=False),
    sa.Column('project_name', sa.String(length=255), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['filament_id'], ['filament_roll.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('print_job')
    op.drop_table('temp_print_job')
    op.drop_table('filament_roll')
    # ### end Alembic commands ###
