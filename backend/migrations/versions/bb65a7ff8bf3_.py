"""empty message

Revision ID: bb65a7ff8bf3
Revises: 
Create Date: 2024-09-11 19:37:57.969097

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bb65a7ff8bf3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('database',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('framework',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('order_status',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('programming_language',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('role',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('service',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('programming_language_id', sa.Integer(), nullable=False),
    sa.Column('database_id', sa.Integer(), nullable=False),
    sa.Column('framework_id', sa.Integer(), nullable=False),
    sa.Column('starting_price', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['database_id'], ['database.id'], ),
    sa.ForeignKeyConstraint(['framework_id'], ['framework.id'], ),
    sa.ForeignKeyConstraint(['programming_language_id'], ['programming_language.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('login', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('phone', sa.String(), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('login')
    )
    op.create_table('order',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('service_id', sa.Integer(), nullable=False),
    sa.Column('status_id', sa.Integer(), nullable=False),
    sa.Column('finally_price', sa.Integer(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.Column('finish_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['service_id'], ['service.id'], ),
    sa.ForeignKeyConstraint(['status_id'], ['order_status.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('review',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=True),
    sa.Column('comment', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('review')
    op.drop_table('order')
    op.drop_table('user')
    op.drop_table('service')
    op.drop_table('role')
    op.drop_table('programming_language')
    op.drop_table('order_status')
    op.drop_table('framework')
    op.drop_table('database')
    op.drop_table('category')
    # ### end Alembic commands ###
