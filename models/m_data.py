#models/m_users.py
from sqlalchemy import (
    Column,
    Integer,
    MetaData,
    String,
    Float,
    Table,
)
from sqlalchemy.sql.sqltypes import Date

metadata = MetaData()
Data = Table(
    "dt_heart", metadata,
    Column('_id', Integer, primary_key=True),
    Column('Age', String(255)),
    Column('Sex', String(255)),
    Column('ChestPainType', String(255)),
    Column('RestingBP', Integer),
    Column('Cholesterol', Integer),
    Column('FastingBS', Integer),
    Column('RestingECG', String(255)),
    Column('MaxHR', Integer),
    Column('ExerciseAngina', String(255)),
    Column('Oldpeak', Float),
    Column('ST_Slope', String(255)),
    Column('ExerciseAngina', String(255)),
    Column('HeartDisease', Integer),
)