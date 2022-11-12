#models/m_users.py
from sqlalchemy import (
    Column,
    Integer,
    MetaData,
    String,
    Table,
)
from sqlalchemy.sql.sqltypes import Date

metadata = MetaData()
User = Table(
    "dt_users", metadata,
    Column('id_users', String(255), primary_key=True),
    Column('name', String(255), nullable=False),
    Column('address', String(255)),
    Column('date_of_birth', Date()),
    Column('telp', String(255)),
    Column('email', String(255)) 
)