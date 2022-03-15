import database.sqlite_db
import CustomLogger
import path

logger = CustomLogger.getLogger(name="CustomLogger")
logger.setLevel(20)


def main():
    db_path = path.get_path("./db/test.db")

    sqlite = database.sqlite_db.SQLite(file_path=db_path)

    sqlite.create_table(table_name="employees", id="integer PRIMARY KEY", firstname="text", lastname="text")
    sqlite.add_column(table_name="employees", column="age", data_type="integer")

    sqlite.get_master_data()

    sqlite.insert(table_name="employees", firstname="Henrik", lastname="Schletter", age=34)
    sqlite.insert(table_name="employees", firstname="Max", lastname="Mustermann", age=99)
    sqlite.insert(table_name="employees", firstname="Hans", lastname="Maier", age=60)

    for line in sqlite.select(table_name="employees"):
        print(line)


if __name__ == '__main__':
    main()
