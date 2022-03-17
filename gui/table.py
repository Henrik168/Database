import tkinter as tk
import logging

logger = logging.getLogger(name="CustomLogger")

class Table(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.canvas = tk.Canvas(self, borderwidth=0)
        self.frame = tk.Frame(self.canvas)
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4, 4), window=self.frame, anchor="nw",
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)


    def onFrameConfigure(self, event):
        """Reset the scroll region to encompass the inner frame"""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def draw_table(self, data: list[dict], column_width: int = 10):

        for widgets in self.frame.winfo_children():
            widgets.destroy()
        self.frame.pack_forget()

        if not data:
            return

        for i, key in enumerate(data[0].keys()):
            tk.Label(self.frame, text=key, width=column_width).grid(row=0, column=i)

        for idy, row in enumerate(data):
            for idx, column in enumerate(row.values()):
                tk.Label(self.frame,
                         text=column,
                         width=column_width,
                         borderwidth="1",
                         relief="solid").grid(row=idy + 1, column=idx)

        self.pack(side="top", fill="both", expand=True)
