from fastapi import Depends, APIRouter

from app.server.auth.authorize import TokenBearer
from app.database.datasource_database import get_database

router = APIRouter(tags=["Data Operations"])


@router.get("/data")
async def get_data(database=Depends(get_database)) -> dict:
    return {"users": database.get_data()}
