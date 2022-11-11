from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  
from routes.r_users import user
from routes.r_nosql_users import user_nosql

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
        "Message": "Codename - Neural"
    }
app.include_router(user)
app.include_router(user_nosql)

