"""Initial commit

Revision ID: 39edc99097c2
Revises: 
Create Date: 2024-10-22 12:24:00.398016

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "39edc99097c2"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "authors",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=155), nullable=True),
        sa.Column("bio", sa.String(length=500), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_index(op.f("ix_authors_id"), "authors", ["id"], unique=False)
    op.create_table(
        "books",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=155), nullable=False),
        sa.Column("summary", sa.String(length=1000), nullable=False),
        sa.Column("publication_date", sa.Date(), nullable=False),
        sa.Column("author_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["author_id"],
            ["authors.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_books_id"), "books", ["id"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_books_id"), table_name="books")
    op.drop_table("books")
    op.drop_index(op.f("ix_authors_id"), table_name="authors")
    op.drop_table("authors")
    # ### end Alembic commands ###
