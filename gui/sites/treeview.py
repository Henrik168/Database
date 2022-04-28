import tkinter as tk
from tkinter import ttk
import logging

logger = logging.getLogger(name="CustomLogger")


class TreeView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.parent = parent
        self.controller = controller
        self.tree = None

    def draw_table(self, data: list[dict]) -> None:

        """ Seems not have a effect"""
        #if self.tree:
            #for widgets in self.tree.winfo_children():
                #widgets.destroy()
            #self.tree.pack_forget()

        if not data:
            self.pack_forget()
            return

        columns = [column for column in data[0].keys()]
        self.tree = ttk.Treeview(self, columns=columns, show="tree headings")

        # format columns
        self.tree.column(column="#0", anchor=tk.CENTER, width=10, minwidth=10)
        for column in data[0].keys():
            self.tree.column(column=column, anchor=tk.CENTER, width=120, minwidth=25)

        # format headings
        self.tree.heading(column="#0", text="", anchor=tk.CENTER)
        for column in data[0].keys():
            self.tree.heading(column=column, text=column, anchor=tk.CENTER)

        # add Data to tree view
        for id_row, row in enumerate(data):
            values = [value for value in row.values()]
            self.tree.insert(parent='', index=tk.END, iid=str(id_row), text="", values=values)
            if (id_row % 2) == 0:
                self.tree.insert(parent=str(id_row), index=tk.END, iid=str(id_row + 100), text="Parent", values=values)

        # Bind Click Event
        self.tree.bind('<<TreeviewSelect>>', self.item_selected)

        self.tree.grid(row=0, column=0, sticky='nsew')

        # add scrollbar to treeview
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

        self.pack()

    def item_selected(self, event):
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            record = [str(item) for item in item["values"]]
            logger.info(f"Selected Dataset: {record}")
            self.controller.show_dataset(table_name="Test", dataset=record)
