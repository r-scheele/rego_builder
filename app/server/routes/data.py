from fastapi import APIRouter, Depends


from app.server.auth.authorize_token import TokenBearer

router = APIRouter(tags=["Data Operations"])


@router.get("/data")
async def get_data(dependencies=Depends(TokenBearer())) -> dict:
    from app.database.datasource_database import get_database

    data = {
        "sql_query": "SELECT DISTINCT groupname AS value FROM geostore.gs_usergroup",
    }
    query = data["sql_query"]
    res_key = query.split(" ")[-1].replace("gs_", "")

    return {res_key: get_database().get_data(query)}
