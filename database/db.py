from abc import ABC, abstractmethod


class DB(ABC):
    @abstractmethod
    def __init__(self, file_path: str) -> None:
        """ Creates a database object."""

    @abstractmethod
    def create_table(self, table_name: str) -> None:
        """ Creates a table in a given database """

    @abstractmethod
    def add_column(self, table_name: str, column: str, data_type: str) -> None:
        """Adds a column to a given table."""

    @abstractmethod
    def insert(self, table_name: str, kwargs: any) -> None:
        """Inserts key word arguments into given table."""

    @abstractmethod
    def delete(self, table_name: str, where: str) -> None:
        """deletes all items in a given table which pass the filter."""

    @abstractmethod
    def update(self, table_name: str, where: str, kwargs: any) -> None:
        """deletes all items in a given table which pass the filter."""

    @abstractmethod
    def select(self, table_name: str, where: str) -> list:
        """deletes all items in a given table which pass the filter."""

