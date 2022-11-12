
import os
from fastapi import FastAPI, Body, HTTPException, status, APIRouter
from fastapi.responses import Response, JSONResponse
from fastapi.encoders import jsonable_encoder
from schemas.s_nosql_users import UserSchema, UpdateUserSchema
from typing import Optional, List
import motor.motor_asyncio


user_nosql = APIRouter()
client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
db = client.users

@user_nosql.post("/nosql/user/", response_description="Add new user", response_model=UserSchema, tags=["NoSQL Database"])
async def create_user(user: UserSchema = Body(...)):
    user = jsonable_encoder(user)
    new_user = await db["users"].insert_one(user)
    created_user = await db["users"].find_one({"_id": new_user.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_user)


@user_nosql.get(
    "/nosql/user/", response_description="List all users", response_model=List[UserSchema], tags=["NoSQL Database"]
)
async def list_users():
    users = await db["users"].find().to_list(1000)
    return users


@user_nosql.get(
    "/nosql/user/{id}", response_description="Get a single user", response_model=UserSchema, tags=["NoSQL Database"]
)
async def show_user_with_id(id: str):
    if (user := await db["users"].find_one({"_id": id})) is not None:
        return user

    raise HTTPException(status_code=404, detail=f"User {id} not found")


@user_nosql.put("/nosql/user/{id}", response_description="Update a user", response_model=UserSchema, tags=["NoSQL Database"])
async def update_user(id: str, user: UpdateUserSchema = Body(...)):
    user = {k: v for k, v in user.dict().items() if v is not None}

    if len(user) >= 1:
        update_result = await db["users"].update_one({"_id": id}, {"$set": user})

        if update_result.modified_count == 1:
            if (
                updated_user := await db["users"].find_one({"_id": id})
            ) is not None:
                return updated_user

    if (existing_user := await db["users"].find_one({"_id": id})) is not None:
        return existing_user

    raise HTTPException(status_code=404, detail=f"User {id} not found")


@user_nosql.delete("/nosql/user/{id}", response_description="Delete a user", tags=["NoSQL Database"])
async def delete_user(id: str):
    delete_result = await db["users"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"User {id} not found")
