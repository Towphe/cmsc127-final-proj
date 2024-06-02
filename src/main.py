import mariadb
import sys
import tkinter as tk
import pandas as pd
from util.repository import Repository
from pages.home import render_home
from pages.establishments import *
from pages.establishment_reviews import *
from pages.foods import *
from pages.food_reviews import *
from pages.auth import *
from pages.reports import *

repository = Repository()

class app:
    def __init__(self, master: tk.Tk):
        self.master = master
        self.username = None
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
        render_home(self.username, self.establishments, self.food_items, self.signin, self.signup, self.signout, self.reports_root, self.establishment_reviews, self.food_reviews)

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

    def reports_root(self):
        self.clear_page()

        render_reports_root(self.home)

    # Establishments
    def establishments(self):
        self.clear_page()
        establishments:pd.DataFrame = repository.Establishment.get_establishments()
        render_establishments(self.username, establishments, self.add_establishment, self.home, self.master, self.edit_establishment, self.review_establishment, repository, self.clear_page, self.establishments)
    
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
    
    def review_establishment(self, establishment_id):
        self.clear_page()

        if self.username == None:
            self.establishments()
            return

        render_review_establishment( establishment_id, self.username, self.establishments, repository, self.master, self.establishments)


    # Food items
    def food_items(self):
        self.clear_page()
        food_items:pd.DataFrame = repository.Food.get_food()
        render_foods(self.username, food_items, self.home, self.master, repository, self.clear_page, self.add_food_item, self.edit_food_item, self.food_items, self.review_food)
    
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
        
    
    def review_food(self, food_id, establishment_id):
        if self.username == None:
            self.food_items()
            return

        render_review_food( food_id, establishment_id, self.username,  self.food_items, repository, self.master,  self.food_items)

    # ESTABLISHMENT REVIEWS
    def establishment_reviews(self):
        self.clear_page()
        establishment_reviews:pd.DataFrame = repository.Establishment.get_all_establishment_reviews()
        render_establishment_reviews(self.username, establishment_reviews, self.home, self.master, self.edit_establishment_review, repository, self.clear_page, self.establishment_reviews)

    def edit_establishment_review(self, review_id, establishment_id):
        self.clear_page()

        if self.username == None:
            self.establishment_reviews()
            return

        render_edit_establishment_review(review_id, establishment_id, self.establishment_reviews,  repository, self.master, self.establishment_reviews)

    # FOOD REVIEWS
    def food_reviews(self):
        self.clear_page()
        food_reviews:pd.DataFrame = repository.Food.get_all_food_reviews()
        render_food_reviews(self.username, food_reviews, self.home, self.master, self.edit_food_review, repository, self.clear_page, self.food_reviews)

    def edit_food_review(self, review_id, food_id):
        self.clear_page()

        if self.username == None:
            self.food_reviews()
            return

        render_edit_food_review(review_id, food_id, self.food_reviews,  repository, self.master, self.food_reviews)
    
    # REPORTS
    def reports_root(self):
        self.clear_page()
        render_reports_root(self.home, self.view_all_food_establishments, self.view_establishments_with_high_rating, self.view_all_reviews, self.view_foods_from_establishment)
    
    def view_all_food_establishments(self):
        self.clear_page()
        establishments = repository.Reports.view_all_food_establishments()
        render_view_all_establishments(self.reports_root, establishments)
    
    def view_establishments_with_high_rating(self):
        self.clear_page()
        establishments = repository.Reports.establishments_with_high_average_rating()
        render_establishments_with_high_average_ratings(self.reports_root, establishments)
    
    def view_all_reviews(self):
        self.clear_page()
        all_reviews:pd.DataFrame = repository.Reports.get_all_reviews_with_name()
        render_all_reviews(self.reports_root, all_reviews)

    def view_foods_from_establishment(self):
        self.clear_page()
        establishments:pd.DataFrame = repository.Establishment.get_establishments()
        food_items:pd.DataFrame = repository.Food.get_food()

        render_foods_from_establishment(self.reports_root, establishments, food_items, repository)

    def view_reviews_for_establishment(self):
        self.clear_page()
        render_reviews_for_establishment(self.reports_root, self.clear_page)

    def view_reviews_for_food_item(self):
        self.clear_page()
        render_reviews_for_food_item(self.reports_root, self.clear_page)

    def view_food_items_from_establishments(self):
        self.clear_page()
        render_food_items_from_establishment(self.reports_root, self.clear_page)

    def view_food_items_from_establishments_with_category(self):
        self.clear_page()
        render_food_items_from_establishment_with_category(self.reports_root, self.clear_page)

    def view_establishment_reviews_within_month(self):
        self.clear_page()
        d = datetime.datetime.now()
        render_establishment_reviews_within_month(self.reports_root, self.clear_page, d.month, d.year)

    def view_food_reviews_within_month(self):
        self.clear_page()
        d = datetime.datetime.now()
        render_food_reviews_within_month(self.reports_root, self.clear_page, d.month, d.year)

    def view_food_items_by_price(self):
        self.clear_page()
        render_food_from_establishment_by_price(self.reports_root, self.clear_page)
    
    def view_food_by_price_range_or_category(self):
        self.clear_page()
        render_food_by_range_and_category(self.reports_root, self.clear_page)

    def reports_root(self):
        self.clear_page()
        render_reports_root(self.home, self.view_all_food_establishments, self.view_establishments_with_high_rating, self.view_reviews_for_establishment, self.view_reviews_for_food_item, self.view_food_items_from_establishments, self.view_food_items_from_establishments_with_category, self.view_establishment_reviews_within_month, self.view_food_reviews_within_month, self.view_food_items_by_price, self.view_food_by_price_range_or_category)

root = tk.Tk()
app(root)
root.mainloop()