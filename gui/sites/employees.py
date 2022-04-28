import tkinter as tk
from gui.sites.treeview import TreeView
import logging

logger = logging.getLogger(name="CustomLogger")


class SearchBar(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.parent = parent
        self.controller = controller

        # label
        self.label = tk.Label(self, text='Search for employees:')
        self.label.grid(row=1, column=0)

        # search entry
        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(self, textvariable=self.search_var, width=30)
        self.search_entry.grid(row=1, column=1, sticky=tk.NSEW)

        # search button
        self.save_button = tk.Button(self, text='Search', command=self.search_button_clicked)
        self.save_button.grid(row=1, column=3, padx=10)

        self.pack()

    def search_button_clicked(self):
        """Handle Button Click Event"""
        if self.controller:
            self.controller.search(table_name="employees", where=self.search_var.get())
        else:
            logger.error(f"Controller not set!")


class Employees(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.parent = parent
        self.controller = controller

        # set up Search Bar
        self.searchbar = SearchBar(self.parent, self.controller)

        # set up Data Table Tree View
        self.table = TreeView(self.parent, controller=self.controller)

    def show_results(self, data: list[dict]):
        self.table.draw_table(data=data)
