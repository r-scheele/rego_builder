import os
import sys
from pathlib import Path

import psycopg2 as pg
import sqlparse
from psycopg2.errors import (
    DuplicateSchema,
    DuplicateTable,
    DuplicateObject,
    UniqueViolation,
    InvalidTableDefinition,
)

from app.config.config import settings

ROOT_DIR = Path(__file__).parent.parent.parent
file_path = os.path.join(ROOT_DIR, "sql", "create_tables.sql")

schema_name = "geostore"
GET_DATA_SQL_COMAND = f"select u.name, g.groupname from {schema_name}.gs_usergroup_members r join {schema_name}.gs_usergroup g on r.group_id = g.id join {schema_name}.gs_user u on r.user_id = u.id;"


class Database:
    def __init__(self) -> None:
        pass

    def connect(self):
        """
        Connect to database and return connection
        """

        try:
            conn = pg.connect(
                database=settings.DATABASE,
                user=settings.DB_USER,
                password=settings.PASSWORD,
                host=f"{settings.HOST},localhost",
            )
            conn.autocommit = True
            return conn.cursor()
        except pg.OperationalError as e:
            sys.exit(1)

    def role_exists(self, role: str) -> bool:
        query = "SELECT 1 FROM pg_catalog.pg_roles WHERE rolname = '{}'".format(role)
        cur = self.connect()
        cur.execute(query)
        res = cur.fetchone()[0]
        return res

    def create_tables(self) -> None:
        """
        Create tables in database
        """
        cursor = self.connect()
        with open(file_path, "r", encoding="utf-8") as file:
            sql = sqlparse.split(sqlparse.format(file.read(), strip_comments=True))
        with cursor:
            for statement in sql:
                try:
                    cursor.execute(statement)
                except (
                    DuplicateSchema,
                    DuplicateTable,
                    DuplicateObject,
                    UniqueViolation,
                    InvalidTableDefinition,
                ) as e:
                    continue

    def get_data(self) -> list:
        cur = self.connect()
        sql = GET_DATA_SQL_COMAND
        cur.execute(sql)
        return cur.fetchall()


database = Database()
database.connect()
if not database.role_exists("geostore"):
    database.create_tables()

data = database.get_data()
