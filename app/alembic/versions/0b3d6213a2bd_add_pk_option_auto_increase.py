"""add pk option - auto increase

Revision ID: 0b3d6213a2bd
Revises: 737902c44fef
Create Date: 2023-10-25 14:24:31.299248

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "0b3d6213a2bd"
down_revision: Union[str, None] = "737902c44fef"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
