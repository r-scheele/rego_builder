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

ROOT_DIR = Path(__file__).parent.parent.parent
file_path = os.path.join(ROOT_DIR, "sql", "create_tables.sql")
f = os.path.join(ROOT_DIR, "sql", "test.sql")


class Database:
    def __init__(self):
        self.conn = self.connect()
        self.create_tables()

    def connect(self):
        """
        Connect to database and return connection
        """
        try:
            conn = pg.connect(
                host="localhost",
                port=5432,
                database="datasource",
                user="postgres",
                password="postgres",
            )
            conn.autocommit = True
        except pg.OperationalError as e:
            sys.exit(1)

        return conn

    def role_exists(self, role_name):
        sql = f"SELECT * FROM pg_roles WHERE rolename = '{role_name}'"
        cur = self.conn.cursor()
        cur.execute(sql)
        return cur.fetchone()[0] is not None

    def create_tables(self):
        """
        Create tables in database
        """
        with self.conn.cursor() as cursor:
            with open(file_path, "r", encoding="utf-8") as file:
                sql = sqlparse.split(sqlparse.format(file.read(), strip_comments=True))

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
        schema_name = "geostore"
        sql = f"select u.name, g.groupname from {schema_name}.gs_usergroup_members r join {schema_name}.gs_usergroup g on r.group_id = g.id join {schema_name}.gs_user u on r.user_id = u.id;"
        cur = self.conn.cursor()
        cur.execute(sql)
        return cur.fetchall()
