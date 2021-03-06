"""ne sdal 1.9

Revision ID: 8fed9b717722
Revises: 3497f65c80f5
Create Date: 2021-11-11 14:35:21.345073

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8fed9b717722'
down_revision = '3497f65c80f5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('action',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), nullable=True),
    sa.Column('content', sa.VARCHAR(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=45), nullable=True),
    sa.Column('first_name', sa.VARCHAR(length=45), nullable=True),
    sa.Column('last_name', sa.VARCHAR(length=50), nullable=True),
    sa.Column('email', sa.VARCHAR(length=255), nullable=True),
    sa.Column('password', sa.VARCHAR(length=100), nullable=True),
    sa.Column('phone', sa.VARCHAR(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('note',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.VARCHAR(length=50), nullable=True),
    sa.Column('content', sa.VARCHAR(length=500), nullable=True),
    sa.Column('tag', sa.VARCHAR(length=20), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('connected_user',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('note_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['note_id'], ['note.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'note_id')
    )
    op.create_table('note_log',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('note_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('action_id', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['action_id'], ['action.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['note_id'], ['note.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('note_log')
    op.drop_table('connected_user')
    op.drop_table('note')
    op.drop_table('user')
    op.drop_table('action')
    # ### end Alembic commands ###
