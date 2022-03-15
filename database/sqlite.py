import logging
import sqlite3

import database.context_manager

logger = logging.getLogger("CustomLogger")


def create_table(db_path: str, table_name: str, table_fields=None) -> None:
    sql_statement = f"CREATE TABLE {table_name} (id INTEGER NOT NULL PRIMARY KEY)"
    with database.context_manager.SQLite(db_path) as cursor:
        try:
            cursor.execute(sql_statement)
            logger.info(f"Table '{table_name}' in database '{db_path}' created. ")
        except sqlite3.OperationalError as e:
            logger.warning(f"{e} in database '{db_path}'")


def add_column(db_path: str, table_name: str, column: str, data_type: str) -> None:
    """
    Adds a Coloumn to an existing Table
    :param db_path:
    :param table_name:
    :param column:
    :param data_type:
    :return:
    """
    sql_statement = f"ALTER TABLE {table_name} ADD COLUMN {column} {data_type}"
    with database.context_manager.SQLite(db_path) as cursor:
        try:
            cursor.execute(sql_statement)
            logger.info(f"Column '{column}' added to '{table_name}' in database '{db_path}' created. ")
        except sqlite3.OperationalError as e:
            logger.warning(f"{e} in database '{db_path}'")


def get_master_data(db_path: str):
    with database.context_manager.SQLite(db_path) as cursor:
        master_query = "SELECT * FROM sqlite_master"
        cursor.execute(master_query)
        table_list = cursor.fetchall()

    for table in table_list:
        logger.info("Database Object Type: %s" % (table[0]))
        logger.info("Database Object Name: %s" % (table[1]))
        logger.info("Table Name: %s" % (table[2]))
        logger.info("Root page: %s" % (table[3]))
        logger.info("**SQL Statement**: %s" % (table[4]))
