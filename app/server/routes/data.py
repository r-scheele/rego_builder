from fastapi import APIRouter, Depends


from app.server.auth.authorize import TokenBearer

router = APIRouter(tags=["Data Operations"])


@router.get("/data")
async def get_data(dependencies=Depends(TokenBearer())) -> dict:
    from app.database.datasource_database import get_database

    data = {
        "sql_query": "SELECT DISTINCT groupname AS value FROM geostore.gs_usergroup;",
    }
    return {"usergroups": get_database().get_data(data["sql_query"])}
