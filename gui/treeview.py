import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import logging

logger = logging.getLogger(name="CustomLogger")


class TreeView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.tree = ttk.Treeview(self)

    def draw_table(self, data: list[dict], column_width: int = 10):

        for widgets in self.tree.winfo_children():
            widgets.destroy()
        self.tree.pack_forget()

        if not data:
            return
        columns = [column for column in data[0].keys()]
        self.tree = ttk.Treeview(self, columns=columns,show="headings")

        # format columns
        self.tree.column(column="#0", anchor=tk.CENTER, width=120, minwidth=25)
        for column in data[0].keys():
            self.tree.column(column=column, anchor=tk.CENTER, width=120, minwidth=25)

        # format headings
        self.tree.heading(column="#0", text="Expand", anchor=tk.CENTER)
        for column in data[0].keys():
            self.tree.heading(column=column, text=column, anchor=tk.CENTER)

        # add Data to tree view
        for id_row, row in enumerate(data):
            values = [value for value in row.values()]
            self.tree.insert(parent='', index=tk.END, iid=str(id_row), text="Parent", values=values)
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
            record =[str(item) for item in item["values"]]
            # show a message
            logger.info(f"Selected Dataset: {record}")
            messagebox.showinfo(title='Information', message=','.join(record))

