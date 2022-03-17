import tkinter as tk


class Table(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

    def draw_table(self, data: list[dict], column_width: int = 10):

        if not data:
            return

        for widgets in self.winfo_children():
            widgets.destroy()

        for i, key in enumerate(data[0].keys()):
            e = tk.Entry(self, width=column_width)
            e.grid(row=0, column=i)
            e.insert(tk.END, key)

        for idy, row in enumerate(data):
            for idx, column in enumerate(row.values()):
                e = tk.Entry(self, width=column_width)
                e.grid(row=idy + 1, column=idx)
                e.insert(tk.END, column)
