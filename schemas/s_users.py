from datetime import date
from pydantic import BaseModel, Field
from typing import List

class UserSchema(BaseModel):
        id_users: str = Field(..., min_lenght=3, max_length=255)
        name: str = Field(..., min_lenght=3, max_length=255)
        address: str = Field(..., min_lenght=3, max_length=255)
        date_of_birth: date = Field(...)
        telp: str = Field(..., min_lenght=3, max_length=255)
        email: str = Field(..., min_lenght=3, max_length=255)

class User(UserSchema):
    id_users: int
    
#list Users
class Users(BaseModel):
    limit: int = Field(default=5)
    offset: int = Field(default=0)
    data: List[User]