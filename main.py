from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  
from routes.r_data import data
from routes.r_export import export

#we will focus on sql first
#from routes.r_nosql_users import user_nosql

app = FastAPI()

def cors_headers(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True,
        )
    return app

@app.get("/", tags=["Root"])
async def root():
    return {
        "Message": "Codename - Neural",
        "Author" : "Farhan Aulianda"
    }
app.include_router(data)
#app.include_router(user_nosql)
app.include_router(export)

