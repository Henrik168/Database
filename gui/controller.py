import logging

logger = logging.getLogger(name="CustomLogger")


class Controller:
    # ToDo: How to add Typehints?
    def __init__(self, model, view):
        self.model = model
        self.view = view
        pass

    def search(self, table_name:str, where: str) -> None:
        try:
            data = self.model.search(table_name=table_name, where=where)
            self.view.show_success(f"Returning {len(data)} Lines.")

        except ValueError as e:
            self.view.show_error(e)


