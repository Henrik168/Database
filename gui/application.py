import tkinter as tk

from database.sqlite_db import SQLite
from gui.model import Model
from gui.controller import Controller
from gui.view import View


class Application(tk.Tk):
    def __init__(self, title: str, db: SQLite, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title(title)
        self.protocol("WM_DELETE_WINDOW", self.end)
        self.db = db

        # Set up MVC
        self.model = Model(db=self.db)
        self.view = View(parent=self)
        self.controller = Controller(model=self.model, view=self.view)
        self.view.set_controller(controller=self.controller)

    def end(self):
        self.destroy()
