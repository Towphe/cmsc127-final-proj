import mariadb
import sys
import tkinter as tk
import pandas as pd
from util.repository import Repository
from pages.home import render_home
from pages.establishments import *
from pages.auth import *

repository = Repository()

def test():
    print("In callback!")

class app:
    def __init__(self, master: tk.Tk):
        self.master = master
        self.username = None
        self.password = None
        self.home()
    
    def clear_page(self):
        for i in self.master.winfo_children():
            i.destroy()

    def home(self):
        self.clear_page()
        render_home(self.username, self.establishments, self.signin)

    def signin(self):
        self.clear_page()
        render_signin(self.home)

    def establishments(self):
        self.clear_page()
        establishments:pd.DataFrame = repository.Establishment.get_establishments()
        render_establishments(establishments, self.add_establishment, self.home, self.master)
    
    def add_establishment(self):
        self.clear_page()
        render_add_establishment(self.establishments, self.master)

root = tk.Tk()
app(root)
root.mainloop()