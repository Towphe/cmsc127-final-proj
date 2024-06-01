import mariadb
import sys
import tkinter as tk
import pandas as pd
from util.repository import Repository
from pages.home import render_home
from pages.establishments import *
from pages.auth import *
from pages.foods import *
from pages.reports import *

repository = Repository()

class app:
    def __init__(self, master: tk.Tk):
        self.master = master
        self.username = "tope"
        self.password = None
        self.home()
    
    def clear_page(self):
        for i in self.master.winfo_children():
            i.destroy()

    def set_user(self, username:str, password:str):
        self.username = username
        self.password = password
        self.home()

    def home(self):
        self.clear_page()
        render_home(self.username, self.establishments, self.food_items, self.signin, self.signup, self.signout, self.reports_root)

    def signin(self):
        self.clear_page()
        render_signin(self.home, repository, self.set_user, self.clear_page)
    
    def signup(self):
        self.clear_page()
        render_signup(self.home, repository, self.set_user, self.clear_page)

    def signout(self):
        self.clear_page()
        self.username = None
        self.password = None
        self.home()

    def establishments(self):
        self.clear_page()
        establishments:pd.DataFrame = repository.Establishment.get_establishments()
        render_establishments(self.username, establishments, self.add_establishment, self.home, self.master, self.edit_establishment, repository, self.clear_page, self.establishments)
    
    def add_establishment(self):
        self.clear_page()

        if self.username == None:
            self.establishments()
            return

        render_add_establishment(self.username, self.establishments, repository, self.master, self.establishments)
    
    def edit_establishment(self, establishment_id):
        self.clear_page()

        if self.username == None:
            self.establishments()
            return

        render_edit_establishment(establishment_id, self.establishments, repository, self.master, self.establishments)
    
    def food_items(self):
        self.clear_page()
        food_items:pd.DataFrame = repository.Food.get_food()
        render_foods(self.username, food_items, self.home, self.master, repository, self.clear_page, self.add_food_item, self.edit_food_item, self.food_items)
    
    def add_food_item(self):
        self.clear_page()
        
        if self.username == None:
            self.food_items()
            return
        
        foods:pd.DataFrame = repository.Food.get_food()

        render_add_food_item(self.username, self.food_items, repository, self.master, self.food_items)
    
    def edit_food_item(self, food_id):
        self.clear_page()

        if self.username == None:
            self.food_items()
            return
        
        render_edit_food_item(food_id, self.food_items, repository, self.master)
    
    def view_all_food_establishments(self):
        self.clear_page()
        establishments = repository.Reports.view_all_food_establishments()
        render_view_all_establishments(self.reports_root, establishments)
    
    def view_establishments_with_high_rating(self):
        self.clear_page()
        establishments = repository.Reports.establishments_with_high_average_rating()
        render_establishments_with_high_average_ratings(self.reports_root, establishments)

    def reports_root(self):
        self.clear_page()
        render_reports_root(self.home, self.view_all_food_establishments, self.view_establishments_with_high_rating)

root = tk.Tk()
app(root)
root.mainloop()