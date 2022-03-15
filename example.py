import os
import sqlite3

import database.sqlite
import CustomLogger

logger = CustomLogger.getLogger(name="CustomLogger")


def main():
    database.sqlite.create_table(db_path="./db/test.db", table_name="tbl_2")


if __name__ == '__main__':
    main()

