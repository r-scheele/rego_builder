import os
import sys
from pathlib import Path

import psycopg2 as pg
import sqlparse
from psycopg2.errors import (
    DuplicateObject,
    DuplicateSchema,
    DuplicateTable,
    InvalidTableDefinition,
    UniqueViolation,
)

from app.config.config import settings

ROOT_DIR = Path(__file__).parent.parent.parent
file_path = os.path.join(ROOT_DIR, "sql", "create_tables.sql")


class DatasourceDatabase:
    """Postgres database functions"""

    def __init__(self) -> None:
        pass

    def connect_database(self):
        """
        Connect to database and return connection object

        params: None
        return: connection cursor object
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
        """
        Check for table existence in database

        :params role: role to be checked
        :returns: True if the role exists, False otherwise
        """

        query = "SELECT 1 FROM pg_catalog.pg_roles WHERE rolname = '{}'".format(role)
        cur = self.connect_database()
        cur.execute(query)
        res = cur.fetchone()[0]
        return res

    def create_tables(self) -> None:
        """
        Create tables in database
        """
        cursor = self.connect_database()
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

    def get_data(self, sql: str) -> dict:
        """
        Get user data from database

        :params sql: sql query
        :returns: List of user group names
        """

        cur = self.connect_database()
        cur.execute(sql)
        data = [value[0] for value in cur.fetchall()]
        return data


database = DatasourceDatabase()
database.connect_database()
if not database.role_exists("geostore"):
    database.create_tables()


def get_database() -> DatasourceDatabase:
    """Return database object for dependency injection"""
    return database
