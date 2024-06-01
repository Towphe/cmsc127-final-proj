import mariadb
import sys
import pandas as pd
import numpy as np
from sqlalchemy import create_engine, Engine
from sqlalchemy.sql import text

class ReportsHandler:
    def __init__(self, db_connection: Engine):
        self.db_connection = db_connection
    
    def view_all_food_establishments(self):     #1
        establishments = pd.read_sql('SELECT * FROM establishment', con=self.db_connection)
        return establishments
    
    def get_all_reviews_with_name(self):   #2
        reviews = pd.read_sql(f'''
                            SELECT food_name AS review_for, reviewer_username, content, rating, date_created 
                            FROM food_review NATURAL JOIN food_item
                            
                            UNION
                            
                            SELECT establishment_name AS review_for, reviewer_username, content, rating, date_created 
                            FROM food_review NATURAL JOIN establishment''', con=self.db_connection)
        return reviews
        
    def all_food_items_from_establishment(self, establishment_id:int):      #3
        foods = pd.read_sql(f"SELECT * FROM food_item WHERE establishment_id = {establishment_id} ", con=self.db_connection)
        return foods
    
    def food_item_from_establishment_from_category(self, establishment_id, category):       #4
        foods = pd.read_sql(f"SELECT * FROM food WHERE establishment_id = {establishment_id} AND category = {category} ", con=self.db_connection)
        return foods

    def establishment_reviews_within_month(self, establishment_id, month:int, year:int):     #5
        reviews = pd.read_sql(f"SELECT * FROM establishment_review WHERE MONTH(review_date) = {month} AND YEAR(review_date) = {year} | set current year by default (?) AND establishment_id = '{establishment_id}'", con=self.db_connection)
        return reviews

    def food_reviews_within_month(self, food_id, month:int, year:int):     #5
        reviews = pd.read_sql(f"SELECT * FROM food_review WHERE MONTH(review_date) = {month} AND YEAR(review_date) = {year} | set current year by default (?) AND food_id = '{food_id}'", con=self.db_connection)
        return reviews

    def establishments_with_high_average_rating(self):  # 6
        establishments = pd.read_sql(f"SELECT * FROM establishment WHERE average_rating >= 4 ORDER BY average_rating DESC", con=self.db_connection)
        return establishments

    def food_items_from_establishment_by_price(self, establishment_id:int): #7
        foods = pd.read_sql(f"SELECT * FROM food_item WHERE establishment_id = {establishment_id} ORDER BY price ", con=self.db_connection)
        return foods

    #8
    def food_items_by_price_range(self, min_price:float, max_price:float):
        foods = pd.read_sql(f"SELECT * FROM food WHERE price BETWEEN {min_price} AND {max_price} ", con=self.db_connection)
        return foods
    
    def food_by_category(self, category:str):
        foods = pd.read_sql(f"SELECT * FROM food WHERE category = '{category}' ", con=self.db_connection)
        return foods
    
    def food_by_price_range_and_category(self, category:str, min_price:float, max_price:float):
        foods = pd.read_sql(f"SELECT * FROM food WHERE (category = '{category}' AND (price BETWEEN {min_price} AND {max_price}) ", con=self.db_connection)
        return foods