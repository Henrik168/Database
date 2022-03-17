import logging
from database.sqlite_db import SQLite

logger = logging.getLogger(name="CustomLogger")


class Model:
    def __init__(self, db: SQLite):
        self.db = db
        pass

    def search(self, table_name: str, where: str):
        result = []
        try:
            for line in self.db.select(table_name=table_name, where=where):
                logger.debug(line)
                result.append(str(line))

            logger.info(f"returning '{len(result)}' Lines")
            return result
        except ValueError as e:
            raise ValueError(e)
