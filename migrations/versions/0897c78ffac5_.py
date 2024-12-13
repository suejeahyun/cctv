"""empty message

Revision ID: 0897c78ffac5
Revises: 
Create Date: 2024-12-16 14:07:37.203818

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0897c78ffac5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('disabled_vehicle_recognition', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_path', sa.String(length=255), nullable=True))

    with op.batch_alter_table('entry_recognition', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_path', sa.String(length=255), nullable=True))

    with op.batch_alter_table('exit_recognition', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_path', sa.String(length=255), nullable=True))

    with op.batch_alter_table('illegal_parking_vehicle_recognition', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_path', sa.String(length=255), nullable=True))

    with op.batch_alter_table('light_vehicle_recognition', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_path', sa.String(length=255), nullable=True))

    with op.batch_alter_table('reports', schema=None) as batch_op:
        batch_op.alter_column('user_name',
               existing_type=mysql.VARCHAR(length=80),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reports', schema=None) as batch_op:
        batch_op.alter_column('user_name',
               existing_type=mysql.VARCHAR(length=80),
               nullable=True)

    with op.batch_alter_table('light_vehicle_recognition', schema=None) as batch_op:
        batch_op.drop_column('image_path')

    with op.batch_alter_table('illegal_parking_vehicle_recognition', schema=None) as batch_op:
        batch_op.drop_column('image_path')

    with op.batch_alter_table('exit_recognition', schema=None) as batch_op:
        batch_op.drop_column('image_path')

    with op.batch_alter_table('entry_recognition', schema=None) as batch_op:
        batch_op.drop_column('image_path')

    with op.batch_alter_table('disabled_vehicle_recognition', schema=None) as batch_op:
        batch_op.drop_column('image_path')

    # ### end Alembic commands ###
