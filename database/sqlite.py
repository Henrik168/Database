import logging
import os
import sys
import sqlite3

logger = logging.getLogger("CustomLogger")


def get_path(db_path: str) -> str:
    """
    returns an absolut Path.
    :param db_path:
    :return:
    """
    dir_path, file_name = os.path.split(db_path)
    dir_path = os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), dir_path))

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    return os.path.join(dir_path, file_name)


class SQLite:
    def __init__(self, file_path: str):
        """
        Context Manager for SQLite Database connection.
        :param file_name:
        """
        self.file_path = get_path(file_path)
        self.connection = sqlite3.connect(self.file_path)

    def __enter__(self):
        logger.info(f"Establish connection to: {self.file_path}")
        return self.connection.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        logger.info(f"Closing connection to {self.file_path}")
        self.connection.commit()
        self.connection.close()


def create_table(db_path: str, table_name: str, table_fields=None) -> None:
    db_path = get_path(db_path)
    sql_statement = f"CREATE TABLE {table_name} (id INTEGER NOT NULL PRIMARY KEY)"
    with SQLite(db_path) as cursor:
        try:
            cursor.execute(sql_statement)
            logger.info(f"Table '{table_name}' in database '{db_path}' created. ")
        except sqlite3.OperationalError as e:
            logger.warning(f"{e} in database '{db_path}'")
