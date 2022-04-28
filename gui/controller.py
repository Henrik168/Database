import logging

logger = logging.getLogger(name="CustomLogger")


class Controller:
    # ToDo: How to add Typehints?
    def __init__(self, model, view):
        self.model = model
        self.view = view
        pass

    def show_employees(self):
        self.view.main.show_employees()

    def search(self, table_name: str, where: str) -> None:
        try:
            data = self.model.search(table_name=table_name, where=where)
            self.view.show_success(f"Returning {len(data)} Lines.")
            self.view.main.main_frame.show_results(data)
            #self.view.main.show_results(data)

        except ValueError as e:
            self.view.show_error(e)

    def show_dataset(self, table_name, dataset: list) -> None:
        self.view.show_success(message=','.join(dataset))
