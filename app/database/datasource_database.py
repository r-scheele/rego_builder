from fastapi import Depends, HTTPException, APIRouter
import psycopg2 as pg
from psycopg2.errors import (
    DuplicateSchema,
    DuplicateTable,
    DuplicateObject,
    UniqueViolation,
    InvalidTableDefinition,
)

import sqlparse
import os, sys
from pathlib import Path
from app.config.config import settings
from app.server.auth.authorize import TokenBearer


ROOT_DIR = Path(__file__).parent.parent.parent
file_path = os.path.join(ROOT_DIR, "sql", "create_tables.sql")

schema_name = "geostore"
GET_DATA_SQL_COMAND = f"select u.name, g.groupname from {schema_name}.gs_usergroup_members r join {schema_name}.gs_usergroup g on r.group_id = g.id join {schema_name}.gs_user u on r.user_id = u.id;"


class Database:
    def __init__(self):
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
                host=settings.HOST,
            )
            conn.autocommit = True
            return conn.cursor()
        except pg.OperationalError as e:
            print("Error connecting to the Postgres database: ", e)
            sys.exit(1)

    def role_exists(self, role: str):
        query = "SELECT 1 FROM pg_catalog.pg_roles WHERE rolname = '{}'".format(role)
        cur = self.connect()
        cur.execute(query)
        res = cur.fetchone()[0]
        return res

    def create_tables(self):
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

    def get_data(self):
        cur = self.connect()
        sql = GET_DATA_SQL_COMAND
        cur.execute(sql)
        return cur.fetchall()


database = Database()
database.connect()
if not database.role_exists("geostore"):
    database.create_tables()

data = database.get_data()
