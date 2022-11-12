from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId
from typing import Optional, List
from datetime import date

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
    email: EmailStr = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Farhan Aulianda",
                "address": "Banda Aceh",
                "date_of_birth": "1996-07-01",
                "telp": "(+62) 822 8040 7563",
                "email": "farhanauliandastudy@gmail.com"
            }
        }


class UpdateUserSchema(BaseModel):
    name: Optional[str]
    address: Optional[str]
    telp: Optional[str]
    email: Optional[EmailStr]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Farhan Aulianda",
                "address": "Banda Aceh",
                "date_of_birth": "1996-07-01",
                "telp": "(+62) 822 8040 7563",
                "email": "farhanauliandastudy@gmail.com"
            }
        }
