import database.sqlite_db
import CustomLogger
import path
import names
import random

logger = CustomLogger.getLogger(name="CustomLogger")
logger.setLevel(20)


def main():
    db_path = path.get_path("./db/test.db")

    sqlite = database.sqlite_db.SQLite(file_path=db_path)

    sqlite.create_table(table_name="employees", id="integer PRIMARY KEY", firstname="text", lastname="text")
    sqlite.add_column(table_name="employees", column="age", data_type="integer")

    sqlite.get_master_data()

    for _ in range(100):
        sqlite.insert(table_name="employees", firstname=names.get_first_name(), lastname=names.get_last_name(),
                      age=random.randint(20, 100))

    for line in sqlite.select(table_name="employees", where="age > 40"):
        logger.info(line)


if __name__ == '__main__':
    main()
