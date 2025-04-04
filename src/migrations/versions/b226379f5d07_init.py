"""init

Revision ID: b226379f5d07
Revises: 
Create Date: 2025-03-11 21:42:58.618026

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b226379f5d07'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('organizations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('platforms',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('organization_name', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['organization_name'], ['organizations.name'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('locations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('state', sa.Boolean(), nullable=False),
    sa.Column('platform_name', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['platform_name'], ['platforms.name'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('assets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('state', sa.Boolean(), nullable=False),
    sa.Column('location_name', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['location_name'], ['locations.name'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('classifications',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('state', sa.Boolean(), nullable=False),
    sa.Column('asset_name', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['asset_name'], ['assets.name'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('specializations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('bid', sa.Float(), nullable=False),
    sa.Column('classification_name', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['classification_name'], ['classifications.name'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('classification_level',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('level_name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('classification_level_rank', sa.Integer(), nullable=False),
    sa.Column('specialization_name', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['specialization_name'], ['specializations.name'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('classification_level')
    op.drop_table('specializations')
    op.drop_table('classifications')
    op.drop_table('assets')
    op.drop_table('locations')
    op.drop_table('platforms')
    op.drop_table('organizations')
    # ### end Alembic commands ###