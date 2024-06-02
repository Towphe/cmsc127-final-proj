import mariadb
import sys
import pandas as pd
import numpy as np
from sqlalchemy import create_engine, Engine
from sqlalchemy.sql import text

class ReportsHandler:
    def __init__(self, db_connection: Engine):
        self.db_connection = db_connection
    
    def view_all_food_establishments(self):     #1  done
        establishments = pd.read_sql('SELECT * FROM establishment', con=self.db_connection)
        return establishments
    
    def reviews_for_establishment(self, establishment_id:int):      #2  done
        reviews = pd.read_sql(f"SELECT * FROM establishment_review WHERE establishment_id = {establishment_id}", con=self.db_connection)
        return reviews
    
    def reviews_for_food_item(self, food_id:int):      #2   done
        reviews = pd.read_sql(f"SELECT * FROM food_review WHERE food_id = {food_id}", con=self.db_connection)
        return reviews
    
    def food_items_from_establishment(self, establishment_id:int):      #3  done
        foods = pd.read_sql(f"SELECT * FROM food_item WHERE establishment_id = {establishment_id} ", con=self.db_connection)
        return foods
    
    def food_item_from_establishment_from_category(self, establishment_id, category):       #4  done
        foods = pd.read_sql(f"SELECT * FROM food_item WHERE establishment_id = {establishment_id} AND category = '{category}' ", con=self.db_connection)
        return foods

    def establishment_reviews_within_month(self, establishment_id, month:int, year:int):     #5 done
        reviews = pd.read_sql(f"SELECT * FROM establishment_review WHERE MONTH(date_created) = {month} AND YEAR(date_created) = {year} AND establishment_id = {establishment_id}", con=self.db_connection)
        return reviews

    def food_reviews_within_month(self, food_id, month:int, year:int):     #5   done
        reviews = pd.read_sql(f"SELECT * FROM food_review WHERE MONTH(date_created) = {month} AND YEAR(date_created) = {year} AND food_id = {food_id}", con=self.db_connection)
        return reviews

    def establishments_with_high_average_rating(self):  # 6 done
        establishments = pd.read_sql(f"SELECT * FROM establishment WHERE average_rating >= 4 ORDER BY average_rating DESC", con=self.db_connection)
        return establishments

    def food_items_from_establishment_by_price(self, establishment_id:int, by:str = 'ASC'): #7  done
        foods = pd.read_sql(f"SELECT * FROM food_item WHERE establishment_id = {establishment_id} ORDER BY price {by} ", con=self.db_connection)
        return foods

    #8
    def food_items_by_price_range(self, min_price:float, max_price:float):
        foods = pd.read_sql(f"SELECT * FROM food_item WHERE price BETWEEN {min_price} AND {max_price} ", con=self.db_connection)
        return foods
    
    def food_by_category(self, category:str):
        foods = pd.read_sql(f"SELECT * FROM food_item WHERE category = '{category}' ", con=self.db_connection)
        return foods
    
    def food_by_price_range_and_category(self, category:str, min_price:float, max_price:float):
        foods = pd.read_sql(f"SELECT * FROM food_item WHERE (category = '{category}' AND (price BETWEEN {min_price} AND {max_price}) ", con=self.db_connection)
        return foods

    def food_by_price_range_and_or_category(self, category:str, min_price:float, max_price:float):
        if min_price == None or max_price == None:
            if category == None:
                return pd.DataFrame()
            else:
                return self.food_by_category(category)
        else:
            if category == None:
                return self.food_items_by_price_range(min_price, max_price)
            else:
                return self.food_by_price_range_and_category(category, min_price, max_price)
        