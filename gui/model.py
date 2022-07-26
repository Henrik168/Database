import logging
from database.sqlite_db import SQLite

log = logging.getLogger()


class Model:
    def __init__(self, db: SQLite):
        self.db = db
        pass

    def search(self, table_name: str, where: str):
        result = []
        try:
            for line in self.db.select(table_name=table_name, where=where):
                log.debug(line)
                result.append(line)

            log.info(f"returning '{len(result)}' Lines")
            return result
        except ValueError as e:
            raise ValueError(e)
