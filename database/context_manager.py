import sqlite3
import logging


logger = logging.getLogger("CustomLogger")


class SQLite:
    def __init__(self, file_path: str):
        """
        Context Manager for SQLite Database connection.
        :param file_name:
        """
        self.file_path = file_path
        self.connection = sqlite3.connect(self.file_path)

    def __enter__(self):
        logger.info(f"Establish connection to: {self.file_path}")
        return self.connection.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        logger.info(f"Closing connection to {self.file_path}")
        self.connection.commit()
        self.connection.close()
