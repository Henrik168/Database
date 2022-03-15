import database.sqlite
import CustomLogger
import path

logger = CustomLogger.getLogger(name="CustomLogger")


def main():
    dp_path = path.get_path("./db/test.db")
    database.sqlite.create_table(db_path=dp_path, table_name="tbl_2")
    database.sqlite.add_column(db_path=dp_path, table_name="tbl_2", column="name2", data_type="text2")
    database.sqlite.get_master_data(db_path=dp_path)


if __name__ == '__main__':
    main()
