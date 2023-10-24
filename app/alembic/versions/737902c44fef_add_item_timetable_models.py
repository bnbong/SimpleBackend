"""add item, timetable models

Revision ID: 737902c44fef
Revises: 5d53ed830f64
Create Date: 2023-10-24 15:16:45.106613

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "737902c44fef"
down_revision: Union[str, None] = "5d53ed830f64"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "item",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=True),
        sa.Column("price", sa.Integer(), nullable=True),
        sa.Column("owner_id", sa.Integer(), nullable=True),
        sa.Column(
            "created",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["owner_id"],
            ["member.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_item_id"), "item", ["id"], unique=False)
    op.create_index(op.f("ix_item_name"), "item", ["name"], unique=False)
    op.create_index(op.f("ix_item_price"), "item", ["price"], unique=False)
    op.create_table(
        "timetable",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("index", sa.String(length=1024), nullable=True),
        sa.Column("owner_id", sa.Integer(), nullable=True),
        sa.Column("start_date", sa.DateTime(timezone=True), nullable=True),
        sa.Column("end_date", sa.DateTime(timezone=True), nullable=True),
        sa.Column(
            "created",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["owner_id"],
            ["member.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_timetable_id"), "timetable", ["id"], unique=False)
    op.create_index(op.f("ix_timetable_index"), "timetable", ["index"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_timetable_index"), table_name="timetable")
    op.drop_index(op.f("ix_timetable_id"), table_name="timetable")
    op.drop_table("timetable")
    op.drop_index(op.f("ix_item_price"), table_name="item")
    op.drop_index(op.f("ix_item_name"), table_name="item")
    op.drop_index(op.f("ix_item_id"), table_name="item")
    op.drop_table("item")
    # ### end Alembic commands ###