import CustomLogger
import path
from database.sqlite_db import SQLite
from gui.application import Application

logger = CustomLogger.getLogger(name="CustomLogger")
logger.setLevel(20)


def main():
    db_path = path.get_path("./db/test.db")

    sqlite = SQLite(file_path=db_path)

    app = Application(title="MVC Design Pattern", db=sqlite)
    app.minsize(600, 480)
    app.mainloop()


if __name__ == "__main__":
    main()
