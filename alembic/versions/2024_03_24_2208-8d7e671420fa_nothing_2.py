"""add relationship 2

Revision ID: 8d7e671420fa
Revises: 5c1c3c7ef547
Create Date: 2024-03-24 22:08:45.854688

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "8d7e671420fa"
down_revision: Union[str, None] = "5c1c3c7ef547"
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