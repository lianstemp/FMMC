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
        id_users: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
        name: str = Field(..., min_lenght=3, max_length=255)
        address: str = Field(..., min_lenght=3, max_length=255)
        date_of_birth: date = Field(...)
        telp: str = Field(..., min_lenght=3, max_length=255)
        email: str = Field(..., min_lenght=3, max_length=255)

class User(UserSchema):
    id_users: str
    
#list Users
class Users(BaseModel):
    limit: int = Field(default=5)
    offset: int = Field(default=0)
    data: List[User]