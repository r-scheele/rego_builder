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
                host=settings.HOST,
                port=settings.PORT,
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

    def get_data(self, sql: dict) -> dict:
        """
        param: {
            "groups": "SELECT DISTINCT groupname AS value FROM geostore.gs_usergroup;",
            "users": "SELECT DISTINCT name AS value FROM geostore.gs_user;",
        }

        return: {
            "groups": [],
            "users": [],
        }
        """
        cur = self.connect()

        data = {}
        for key, value in sql.items():
            cur.execute(value)
            res = [{"value": r[0]} for r in cur.fetchall()]
            data[key] = res

        return data


database = Database()
database.connect()
if not database.role_exists("geostore"):
    database.create_tables()


def get_database() -> Database:
    return database
