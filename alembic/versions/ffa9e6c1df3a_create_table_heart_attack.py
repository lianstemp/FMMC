"""create table heart-attack

Revision ID: 7368b54ab382
Revises: ffa9e6c1df3a
Create Date: 2022-11-14 21:41:07.751743

"""
from alembic import op
import sqlalchemy as sa
# from faker import Faker 

# faker = Faker('id_ID')


# revision identifiers, used by Alembic.
revision = 'ffa9e6c1df3a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    users = op.create_table(
        'dt_heart',
        sa.Column('_id', sa.Integer, primary_key=True),
        sa.Column('Age', sa.String(255)),
        sa.Column('Sex', sa.String(255)),
        sa.Column('ChestPainType', sa.String(255)),
        sa.Column('RestingBP', sa.Integer),
        sa.Column('Cholesterol', sa.Integer),
        sa.Column('FastingBS', sa.Integer),
        sa.Column('RestingECG', sa.String(255)),
        sa.Column('MaxHR', sa.Integer),
        sa.Column('ExerciseAngina', sa.String(255)),
        sa.Column('Oldpeak', sa.Float),
        sa.Column('ST_Slope', sa.String(255)),
        sa.Column('ExerciseAngina', sa.String(255)),
        sa.Column('HeartDisease', sa.Integer),
    )
    


def downgrade():
    op.drop_table('dt_users')
