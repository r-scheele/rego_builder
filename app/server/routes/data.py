from fastapi import Depends, HTTPException, APIRouter
from app.server.auth.authorize import TokenBearer


router = APIRouter(tags=["Data Operations"])

from app.database.datasource_database import data


@router.get("/data")
async def get_data(dependencies=Depends(TokenBearer())) -> dict:
    return {"users": data}
