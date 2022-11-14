from datetime import date
from pydantic import BaseModel, Field
from bson import ObjectId
from typing import List

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

class UserSchema(BaseModel):  
        _id: int = Field(...)
        Age: str = Field(...)
        Sex: str = Field(...)
        ChestPainType: str = Field(...)
        RestingBP: int = Field(...)
        Cholesterol: int = Field(...)
        FastingBS: int = Field(...)
        RestingECG: str = Field(...)
        MaxHR: int = Field(...)
        ExerciseAngina: str = Field(...)
        Oldpeak: float = Field(...)
        ST_Slope: str = Field(...)
        ExerciseAngina: str = Field(...)
        HeartDisease: int = Field(...)

class Data(UserSchema):
    _id: int
    
#list Datas
class Datas(BaseModel):
    limit: int = Field(default=5)
    offset: int = Field(default=0)
    data: List[Data]