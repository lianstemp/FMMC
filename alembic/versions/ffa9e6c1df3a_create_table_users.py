"""create table users 

Revision ID: ffa9e6c1df3a
Revises: 
Create Date: 2022-11-09 20:33:33.205576

"""
from alembic import op
import sqlalchemy as sa
from faker import Faker 

faker = Faker('id_ID')


# revision identifiers, used by Alembic.
revision = 'ffa9e6c1df3a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    users = op.create_table(
        'dt_users',
        sa.Column('_id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('address', sa.String(255)),
        sa.Column('date_of_birth', sa.Date()),
        sa.Column('telp', sa.String(255)),
        sa.Column('email', sa.String(255), unique=True)
        
    )
    
    op.bulk_insert(
        users,
        [{'name':faker.name(),
                'address':faker.address(),
                'date_of_birth':faker.date_of_birth(tzinfo=None, minimum_age=15, maximum_age=30),
                'telp':faker.phone_number(),
                'email':faker.email()
        } for x in range(100)]
    )


def downgrade():
    op.drop_table('dt_users')
