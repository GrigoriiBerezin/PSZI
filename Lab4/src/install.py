import os
import shutil
import sys
import tkinter as tk
import winreg
import sqlite3 as sql
from tkinter import filedialog as fd

# Сделать ключ со значением того, что программа услановлена
# Сделать инициализацию бд тут
class Installer(tk.Frame):
    COUNTER = 4
    TIME = 60

    install_button = None
    choose_button = None
    path_entry = None
    path = None

    def __init__(self, master=None):
        super().__init__(master)
        self.path = tk.StringVar()
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        tk.Label(self, text="Choose path to install a program") \
            .grid(row=0, column=0, pady=2, sticky=tk.W)

        self.path.set(sys.path[0])
        self.path_entry = tk.Entry(self,
                                   state="readonly",
                                   textvariable=self.path,
                                   width=30)
        self.path_entry.grid(row=1, column=0, pady=2, sticky=tk.W)

        self.choose_button = tk.Button(self)
        self.choose_button["text"] = "Choose path"
        self.choose_button["command"] = self.to_choose
        self.choose_button.grid(row=1, column=2, sticky=tk.W)

        self.install_button = tk.Button(self)
        self.install_button["text"] = "Install"
        self.install_button["command"] = self.to_install
        self.install_button.grid(row=2, column=0, sticky=tk.W)

    def to_choose(self):
        choice = fd.askdirectory()
        self.path.set(choice)

    def to_install(self):
        try:
            reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
            open_key = winreg.OpenKey(reg, "Software", 0, winreg.KEY_WRITE)
            open_key = winreg.CreateKeyEx(open_key, "Lab3")
            winreg.SetValue(open_key, "Counter", winreg.REG_SZ, str(self.COUNTER))
            winreg.SetValue(open_key, "Timer", winreg.REG_SZ, str(self.TIME))
        except PermissionError:
            print("You don't have permission to do this")
            return -1

        path_file = os.path.join(self.path.get(), "executer.lnk")
        sym_path = os.path.join(sys.path[0], "..", "executer.lnk")
        shutil.copy(sym_path, path_file)

        with sql.connect(os.path.join(sys.path[0], "names")) as conn:
            curs = conn.cursor()
            curs.execute("INSERT INTO address VALUES (?)", (path_file,))
            conn.commit()

        self.quit()

    def quit(self):
        self.master.destroy()


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Installer")

    app = Installer(master=root)
    app.mainloop()
