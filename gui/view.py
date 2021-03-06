import logging
import tkinter as tk
from gui.sites.employees import Employees

log = logging.getLogger()
DEBUG: bool = False


class StatusBar(tk.Frame):
    def __init__(self, parent: tk.Misc):
        super().__init__(master=parent)
        self.controller = None
        if DEBUG:
            self.config(bg="red")
        self.pack(side=tk.BOTTOM, fill=tk.X, expand=False)

        # message
        self.message_label = tk.Label(self, text='', foreground='red')
        self.message_label.pack()

    def set_controller(self, controller):
        # ToDo: How to add Typehints?
        self.controller = controller


class NavBar(tk.Frame):
    def __init__(self, parent: tk.Misc):
        super().__init__(master=parent)
        self.parent = parent
        self.controller = None
        if DEBUG:
            self.config(bg="blue")

        # Employees button
        self.employees_button = tk.Button(self, text='Employees', command=self.show_employees)
        self.employees_button.grid(row=1, column=1, pady=10)

        # Settings button
        self.settings_button = tk.Button(self, text='Settings', command=self.show_settings)
        self.settings_button.grid(row=2, column=1, pady=100)

        self.pack(side=tk.LEFT, fill=tk.Y, expand=False)

    def set_controller(self, controller):
        # ToDo: How to add Typehints?
        self.controller = controller

    def show_employees(self):
        self.controller.show_employees()

    def show_settings(self):
        pass


class ToolBar(tk.Frame):
    def __init__(self, parent: tk.Misc):
        super().__init__(master=parent)
        self.controller = None
        if DEBUG:
            self.config(bg="green")
        self.pack(side=tk.TOP, fill=tk.X, expand=False)

        self.add_employee_button = tk.Button(self, text='add Employee', command=self.add_employee)
        self.add_employee_button.pack(side=tk.RIGHT, pady=10, padx=10)

    def set_controller(self, controller):
        # ToDo: How to add Typehints?
        self.controller = controller

    def add_employee(self):
        pass


class Main(tk.Frame):
    def __init__(self, parent: tk.Misc):
        super().__init__(master=parent)
        self.parent = parent
        self.controller = None
        self.main_frame = None
        if DEBUG:
            self.config(bg="yellow")
        self.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    def set_controller(self, controller):
        # ToDo: How to add Typehints?
        self.controller = controller

    def show_employees(self):
        self.main_frame = Employees(self, self.controller)


class View(tk.Frame):
    def __init__(self, parent: tk.Misc):
        super().__init__(parent)
        self.parent = parent
        self.controller = None

        # Define Segments of Frame
        self.statusbar = StatusBar(parent=self.parent)
        self.navbar = NavBar(parent=self.parent)
        self.toolbar = ToolBar(parent=self.parent)
        self.main = Main(parent=self.parent)

    def set_controller(self, controller):
        # ToDo: How to add Typehints?
        self.controller = controller

        self.statusbar.set_controller(controller=self.controller)
        self.navbar.set_controller(controller=self.controller)
        self.toolbar.set_controller(controller=self.controller)
        self.main.set_controller(controller=self.controller)

    def show_error(self, message):
        """Show an Error Message"""
        self.statusbar.message_label['text'] = message
        self.statusbar.message_label['foreground'] = 'red'
        self.statusbar.message_label.after(3000, self.hide_message)

    def show_success(self, message):
        """Show a success message"""
        self.statusbar.message_label['text'] = message
        self.statusbar.message_label['foreground'] = 'green'
        self.statusbar.message_label.after(3000, self.hide_message)

    def hide_message(self):
        """Hide the message"""
        self.statusbar.message_label['text'] = ''
