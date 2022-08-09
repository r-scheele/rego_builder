from app.schemas.data import DataRequest
from fastapi import Depends, APIRouter

from app.server.auth.authorize import TokenBearer


router = APIRouter(tags=["Data Operations"])


@router.post("/data")
async def get_data(data: DataRequest, dependencies=Depends(TokenBearer())) -> dict:
    from app.database.datasource_database import get_database

    res = {}
    for data_query in data.queries:
        sql = {}
        sql[data_query.data_list_name] = data_query.sql_query
        res.update(get_database().get_data(sql))
    return {"data": res}
