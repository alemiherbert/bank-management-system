"""empty message

Revision ID: cf8dca2b0298
Revises: 
Create Date: 2022-09-16 21:42:54.968178

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf8dca2b0298'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('branch',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=True),
    sa.Column('rcode', sa.String(length=4), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_branch_rcode'), 'branch', ['rcode'], unique=True)
    op.create_table('customer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fname', sa.String(length=32), nullable=False),
    sa.Column('lname', sa.String(length=32), nullable=False),
    sa.Column('email', sa.String(length=32), nullable=False),
    sa.Column('phone', sa.String(length=32), nullable=False),
    sa.Column('nin', sa.String(length=32), nullable=False),
    sa.Column('gender', sa.String(length=32), nullable=False),
    sa.Column('d_o_b', sa.Date(), nullable=True),
    sa.Column('address', sa.String(length=128), nullable=False),
    sa.Column('occupation', sa.String(length=32), nullable=False),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.Column('cbranch_id', sa.Integer(), nullable=True),
    sa.Column('ctype', sa.String(length=32), nullable=False),
    sa.Column('joindate', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['cbranch_id'], ['branch.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_customer_ctype'), 'customer', ['ctype'], unique=False)
    op.create_index(op.f('ix_customer_email'), 'customer', ['email'], unique=True)
    op.create_index(op.f('ix_customer_joindate'), 'customer', ['joindate'], unique=False)
    op.create_index(op.f('ix_customer_nin'), 'customer', ['nin'], unique=True)
    op.create_index(op.f('ix_customer_phone'), 'customer', ['phone'], unique=True)
    op.create_index(op.f('ix_customer_status'), 'customer', ['status'], unique=False)
    op.create_table('account',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('kind', sa.String(length=32), nullable=False),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.Column('number', sa.String(length=32), nullable=False),
    sa.Column('balance', sa.String(length=32), nullable=True),
    sa.Column('holder_id', sa.Integer(), nullable=True),
    sa.Column('branch_id', sa.Integer(), nullable=True),
    sa.Column('createdate', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['branch_id'], ['branch.id'], ),
    sa.ForeignKeyConstraint(['holder_id'], ['customer.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_account_createdate'), 'account', ['createdate'], unique=False)
    op.create_index(op.f('ix_account_kind'), 'account', ['kind'], unique=False)
    op.create_index(op.f('ix_account_number'), 'account', ['number'], unique=False)
    op.create_index(op.f('ix_account_status'), 'account', ['status'], unique=False)
    op.create_table('employee',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=32), nullable=False),
    sa.Column('e_id', sa.String(length=32), nullable=False),
    sa.Column('estatus', sa.Integer(), nullable=False),
    sa.Column('ebranch_id', sa.Integer(), nullable=True),
    sa.Column('startdate', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['ebranch_id'], ['branch.id'], ),
    sa.ForeignKeyConstraint(['id'], ['customer.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_employee_e_id'), 'employee', ['e_id'], unique=True)
    op.create_index(op.f('ix_employee_estatus'), 'employee', ['estatus'], unique=False)
    op.create_index(op.f('ix_employee_startdate'), 'employee', ['startdate'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_employee_startdate'), table_name='employee')
    op.drop_index(op.f('ix_employee_estatus'), table_name='employee')
    op.drop_index(op.f('ix_employee_e_id'), table_name='employee')
    op.drop_table('employee')
    op.drop_index(op.f('ix_account_status'), table_name='account')
    op.drop_index(op.f('ix_account_number'), table_name='account')
    op.drop_index(op.f('ix_account_kind'), table_name='account')
    op.drop_index(op.f('ix_account_createdate'), table_name='account')
    op.drop_table('account')
    op.drop_index(op.f('ix_customer_status'), table_name='customer')
    op.drop_index(op.f('ix_customer_phone'), table_name='customer')
    op.drop_index(op.f('ix_customer_nin'), table_name='customer')
    op.drop_index(op.f('ix_customer_joindate'), table_name='customer')
    op.drop_index(op.f('ix_customer_email'), table_name='customer')
    op.drop_index(op.f('ix_customer_ctype'), table_name='customer')
    op.drop_table('customer')
    op.drop_index(op.f('ix_branch_rcode'), table_name='branch')
    op.drop_table('branch')
    # ### end Alembic commands ###