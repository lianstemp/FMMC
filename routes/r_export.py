from fastapi.responses import StreamingResponse
from fastapi import APIRouter
from models.m_data import Data
import pandas as pd
from config.database import conn
from io import BytesIO

export = APIRouter()


@export.get("/download/csv",tags=["Download"])
def download_csv_data(limit: int = 10, offset: int = 0):
    query = Data.select().offset(offset).limit(limit)
    df = pd.DataFrame(conn.execute(query))
    
    return StreamingResponse(
        iter([df.to_csv(index=False)]),
        media_type="text/csv",
        headers={"Content-Disposition": f"attachment; filename=data.csv"}
)

@export.get("/download/xlsx",tags=["Download"])
def download_excel_data(limit: int = 10, offset: int = 0):
    query = Data.select().offset(offset).limit(limit)
    df = pd.DataFrame(conn.execute(query))
    buffer = BytesIO()
    with pd.ExcelWriter(buffer) as writer:
        df.to_excel(writer, index=False)
    return StreamingResponse(
        BytesIO(buffer.getvalue()),
        media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        headers={"Content-Disposition": f"attachment; filename=data.xlsx"}
)

    
