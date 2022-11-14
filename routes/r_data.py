from schemas.s_data import UserSchema, Datas
from models.m_data import Data
from fastapi import APIRouter, Response, status
from config.database import conn

data = APIRouter()

#get all data
@data.get("/data/heart/", response_model=Datas, description="Show All Data Datas", tags=["SQL Database"])
async def list_all_data(limit: int = 10, offset: int = 0):
    query = Data.select().offset(offset).limit(limit)
    data = conn.execute(query).fetchall()
    response = {"limit": limit, "offset": offset, "data": data}
    return response

#Add new Data
@data.post("/data/heart/", description="Add Data", tags=["SQL Database"])
async def create_data(usr: UserSchema, response: Response):
    
    email_check = Data.select().filter(Data.c.email == usr.email)
    email_check = conn.execute(email_check).fetchone()
    
    if email_check is not None:
        
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {
            "status": response.status_code, 
            "message": "Email Already Exists"
        }
        
    query = Data.insert().values(
        name = usr.name,
        address = usr.address,
        date_of_birth = usr.date_of_birth,
        telp = usr.telp,
        email = usr.email
    )
    
    conn.execute(query)
    data = Data.select().order_by(Data.c._id.desc())
    response = {
        "message" : f"Success add new data data", "data": conn.execute(data).fetchone()
    }
    return response

#get data by id
@data.get("/data/heart/{id}", description="Show Details Datas", tags=["SQL Database"])
async def show_data_with_id(id: int, response: Response):
    query = Data.select().where(Data.c._id == id)
    data = conn.execute(query).fetchone()
    if data is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {
            "message" : "Datas Not Found", "Status" : response.status_code
        }
    
    response = {
        "message" : f"Success show data with id {id}", "data": data
    }
    return response


#Edit Data data

@data.put("/data/heart/{id}", description="Edit Data Datas", tags=["SQL Database"])
async def update_data(id: int, usr : UserSchema, response: Response):
    
    email_check = Data.select().filter(Data.c.email == usr.email, Data.c._id != id)
    email_check = conn.execute(email_check).fetchone()
    
    if email_check is not None:
        
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {
            "status": response.status_code, 
            "message": "Email Already Exists"
        }
        
    query = Data.update().values(
        name = usr.name,
        address = usr.address,
        date_of_birth = usr.date_of_birth,
        telp = usr.telp,
        email = usr.email
    ).where(Data.c._id == id)
    
    conn.execute(query)
    print(query)
    data = Data.select().where(Data.c._id == id)
    response = {
        "message" : f"Success change data data with id {id}", "data": conn.execute(data).fetchone()
    }
    return response                    
                            


#Delete Data
@data.delete("/data/heart/{id}", description="Delete Datas Data", tags=["SQL Database"])
async def delete_data(id: int, response: Response):
    query = Data.select().where(Data.c._id == id)
    data = conn.execute(query).fetchone()
    if data is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {
            "message": "Datas Not Found", "Status": response.status_code
        }
    
    query = Data.delete().where(Data.c._id == id)
    conn.execute(query)
    response = {
        "message" : f"Success delete data with id {id}"
    }
    return response