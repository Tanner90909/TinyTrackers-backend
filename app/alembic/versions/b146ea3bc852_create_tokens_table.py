"""create tokens table

Revision ID: b146ea3bc852
Revises: ce0c0714bcc4
Create Date: 2023-11-16 19:58:27.975618

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b146ea3bc852'
down_revision: Union[str, None] = 'ce0c0714bcc4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tokens',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('token_type', sa.String(), nullable=True, default="bearer"),
    sa.Column('access_token', sa.String(), nullable=False),
    sa.Column('user_id', sa.Integer(), sa.ForeignKey("users.id"), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tokens_id'), 'tokens', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_tokens_id'), table_name='users')
    op.drop_table('tokens')
    # ### end Alembic commands ###