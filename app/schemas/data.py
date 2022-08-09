from typing import Dict, List, Optional, Union

from pydantic import BaseModel


class Data(BaseModel):
    data_list_name: str
    sql_query: str


class DataRequest(BaseModel):
    queries: List[Data]

    class Config:
        schema_extra = {
            "example": {
                "queries": [
                    {
                        "data_list_name": "groups",
                        "sql_query": "SELECT DISTINCT groupname AS value FROM geostore.gs_usergroup;",
                    },
                    {
                        "data_list_name": "users",
                        "sql_query": "SELECT DISTINCT name AS value FROM geostore.gs_user;",
                    },
                ]
            }
        }
