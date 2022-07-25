from fastapi import Depends, APIRouter

from app.server.auth.authorize import TokenBearer
from app.database.datasource_database import data

router = APIRouter(tags=["Data Operations"])


@router.get("/data")
async def get_data(dependencies=Depends(TokenBearer())) -> dict:
    return {"users": data}
