"""create guild reports table

Revision ID: e822039a61ba
Revises: 
Create Date: 2024-02-25 23:07:14.618495

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e822039a61ba'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'guild_reports',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('code', sa.String(20), unique=True, nullable=False),
        sa.Column('title', sa.Text),
        sa.Column('startTime', sa.Integer),
        sa.Column('endTime', sa.Integer),
        sa.Column('segments', sa.Integer),
        sa.Column('guild_id', sa.Integer, nullable=False)
    )


def downgrade() -> None:
    pass
