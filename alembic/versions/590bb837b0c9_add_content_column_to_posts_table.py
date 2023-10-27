"""add content column to posts table

Revision ID: 590bb837b0c9
Revises: 17f720963963
Create Date: 2023-10-27 11:22:11.074721

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "590bb837b0c9"
down_revision: Union[str, None] = "17f720963963"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column("posts", "content")
