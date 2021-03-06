import sqlite3
import logging

from database.db import DB

log = logging.getLogger()


class SQLiteCM:
    def __init__(self, file_path: str):
        """
        Context Manager for SQLite Database connection.
        :param file_name:
        """
        self.file_path = file_path
        self.connection = sqlite3.connect(self.file_path)

    def __enter__(self):
        log.debug(f"Establish connection to: {self.file_path}")
        self.connection.row_factory = sqlite3.Row
        return self.connection.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        log.debug(f"Closing connection to {self.file_path}")
        self.connection.commit()
        self.connection.close()


class SQLite(DB):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def create_table(self, table_name: str, **kwargs: any) -> None:
        """
        Creates a table in a given database.
        :param table_name:
        :param kwargs: Keyword = column, Value = datatype
        Example: id = INTEGER NOT NULL PRIMARY KEY,
                 name = INTEGER,
                 age = INTEGER
        :return:
        """
        columns = ", ".join(str(keyword + " " + kwargs[keyword]) for keyword in kwargs.keys())

        sql_statement = f"CREATE TABLE {table_name} ({columns});"

        with SQLiteCM(self.file_path) as cursor:
            try:
                cursor.execute(sql_statement)
                log.info(f"Created Table '{table_name}' in database '{self.file_path}'. ")
            except sqlite3.OperationalError as e:
                log.warning(f"{e} in database '{self.file_path}'")
                log.warning(sql_statement)

    def add_column(self, table_name: str, column: str, data_type: str) -> None:
        sql_statement = f"ALTER TABLE {table_name} ADD COLUMN {column} {data_type};"

        with SQLiteCM(self.file_path) as cursor:
            try:
                cursor.execute(sql_statement)
                log.info(f"Added column '{column}' to '{table_name}' in database '{self.file_path}'. ")
            except sqlite3.OperationalError as e:
                log.warning(f"{e} in database '{self.file_path}'")
                log.warning(sql_statement)
                raise ValueError(e)

    def insert(self, table_name: str, **kwargs: any) -> None:
        keywords = ", ".join(str(keyword) for keyword in kwargs.keys())
        wildcards = ", ".join("?" for _ in kwargs.values())
        values = [str(value) for value in kwargs.values()]
        sql_statement = f"INSERT INTO {table_name}({keywords}) VALUES({wildcards});"

        with SQLiteCM(self.file_path) as cursor:
            try:
                cursor.execute(sql_statement, values)
                log.info(f"Insert '{values}' into '{table_name}' in database '{self.file_path}'. ")
            except sqlite3.OperationalError as e:
                log.warning(f"{e} in database '{self.file_path}'")
                log.warning(sql_statement)
                raise ValueError(e)
            except sqlite3.IntegrityError as e:
                log.warning(f"{e} in database '{self.file_path}'")
                log.warning(sql_statement)
                raise ValueError(e)

    def delete(self, table_name: str, where: str) -> None:
        pass

    def update(self, table_name: str, where: str, kwargs: any) -> None:
        pass

    def select(self, table_name: str, where: str = None) -> list:
        sql_statement = f"SELECT * FROM {table_name}"

        if where:
            sql_statement += " WHERE " + where + ";"

        with SQLiteCM(self.file_path) as cursor:
            try:
                cursor.execute(sql_statement)
                log.info(f"Selected from '{table_name}' in database '{self.file_path}'. ")
                return [dict(row) for row in cursor.fetchall()]
            except sqlite3.OperationalError as e:
                log.warning(f"{e} in database '{self.file_path}'")
                log.warning(sql_statement)
                raise ValueError(e)

    def get_master_data(self):
        with SQLiteCM(self.file_path) as cursor:
            master_query = "SELECT * FROM sqlite_master"
            cursor.execute(master_query)
            table_list = cursor.fetchall()

        for table in table_list:
            log.info("Database Object Type: %s" % (table[0]))
            log.info("Database Object Name: %s" % (table[1]))
            log.info("Table Name: %s" % (table[2]))
            log.info("Root page: %s" % (table[3]))
            log.info("**SQL Statement**: %s" % (table[4]))
