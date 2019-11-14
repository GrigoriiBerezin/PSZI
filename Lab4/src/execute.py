import os
import sys
import tkinter as tk
from tkinter import messagebox
import sqlite3 as sql
import winreg


class Handler(tk.Frame):
    path = sys.path[0]
    conn = sql.connect(os.path.join(path, "names"))
    curs = conn.cursor()
    reg = winreg.OpenKey(
        winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER),
        os.path.join("Software", "Lab3"))
    name = None
    entry = None
    activate = None
    count = None
    count_label = None
    timer_label = None

    PATTERN = "INSERT INTO name(name) VALUES (?)"

    def __init__(self, master=None):
        super().__init__(master)
        self.name = tk.StringVar()
        self.count = tk.IntVar()
        self.timer = tk.IntVar()
        self.check()
        self.create_widgets()
        self.time_handle()
        self.pack()

    def create_widgets(self):
        tk.Label(self, text="Enter your name") \
            .grid(row=0, column=0, pady=2, sticky=tk.W + tk.E)

        self.entry = tk.Entry(self, textvariable=self.name)
        self.entry.grid(row=1, column=0, pady=2)

        self.activate = tk.Button(self)
        self.activate["text"] = "Test"
        self.activate["command"] = self.handle
        self.activate.grid(row=2, column=0, pady=2)

        self.count_label = tk.Label(self, textvariable=self.count)
        self.count_label.grid(row=3, column=0, sticky=tk.W)

        self.timer_label = tk.Label(self, textvariable=self.timer)
        self.timer_label.grid(row=3, column=1, sticky=tk.E)

        self.timer.set(winreg.QueryValue(self.reg, "Timer"))

    def handle(self):
        try:
            self.curs.execute(self.PATTERN, (self.name.get(),))
            self.conn.commit()

            self.count.set(self.count.get() - 1)
            winreg.SetValue(self.reg, "Counter", winreg.REG_SZ, str(self.count.get()))
        except sql.IntegrityError:
            messagebox.showerror("This name is already exist")

        self.check()

    def check(self):
        self.count.set(winreg.QueryValue(self.reg, "Counter"))

        if self.count.get() == 0:
            messagebox.showerror("Trial version is end, buy full version")
            self.master.destroy()

    def time_handle(self):
        if self.timer.get() <= 0:
            self.master.destroy()
        else:
            self.after(1000, self.time_handle)

        self.timer.set(self.timer.get() - 1)
        winreg.SetValue(self.reg, "Timer", winreg.REG_SZ, str(self.timer.get()))


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Handler")

    app = Handler(root)
    app.mainloop()
