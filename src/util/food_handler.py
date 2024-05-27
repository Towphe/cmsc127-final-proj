import mariadb
import sys
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sqlalchemy.sql import text

class FoodHandler:
    def __init__(self, db_connection):
        self.db_connection = db_connection
    
    def get_food(self):
        foods = pd.read_sql('SELECT * FROM food_item', con=self.db_connection)
        return foods
    
    def add_food(self, establishment_id:int, food_name:str, price:float):
        with self.db_connection.connect() as con:
            con.execute(text(f"INSERT INTO food_item (establishment_id, food_name, price) VALUES ({establishment_id}, '{food_name}', {float(price)}); "))
            con.commit()
        return
    
    def remove_food(self, food_id:int):
        with self.db_connection.connect() as con:
            con.execute(text(f"DELETE FROM food_item WHERE food_id = {food_id}; "))
            con.commit()
        return
    
    def update_food(self, food_id:int, food_name:str):
        with self.db_connection.connect() as con:
            con.execute(text(f'''
                            UPDATE food_item 
                            SET food_name = '{food_name}'
                            WHERE food_id = {food_id};
                        '''))
            con.commit()
        return
    
    def create_food_review(self, food_id:int, reviewer:str, content:str, rating:float):
        with self.db_connection.connect() as con:
            con.execute(text(f'''
                            INSERT INTO food_review (food_id, reviewer_username, content, rating)
                            VALUES ({food_id}, '{reviewer}', '{content}', {rating});
                        '''))
            con.commit()
            con.execute(text(f'''
                            UPDATE food_item
                            SET average_rating = (
                                SELECT AVG(rating) 
                                FROM food_review 
                                WHERE food_id = {food_id})
                            WHERE food_id = {food_id};
                             '''))  # this leads to faster reads
            con.commit()
        return
    
    def get_food_reviews(self, food_id:int):
        food_reviews = pd.read_sql(f"SELECT * FROM food_review WHERE food_id = {food_id}", con=self.db_connection)
        return food_reviews
    
    def update_food_review(self, review_id:int, food_id:int, content:str, rating:float):
        with self.db_connection.connect() as con:
            con.execute(text(f'''
                            UPDATE food_review 
                            SET
                                content = '{content}',
                                rating = {rating}
                            WHERE
                                review_id = {review_id};
                        '''))
            con.commit()
            con.execute(text(f'''
                            UPDATE food_item
                            SET average_rating = (
                                SELECT AVG(rating) 
                                FROM food_review 
                                WHERE food_id = {food_id})
                            WHERE food_id = {food_id};
                             '''))  # this leads to faster reads
            con.commit()
        return
    
    def delete_food_review(self, review_id:int, food_id:int):
        with self.db_connection.connect() as con:
            con.execute(text(f'''
                            DELETE FROM food_review 
                            WHERE review_id = '{review_id}';
                        '''))
            con.commit()
            con.execute(text(f'''
                            UPDATE food_item
                            SET average_rating = (
                                SELECT AVG(rating) 
                                FROM food_review 
                                WHERE food_id = '{food_id}')
                            WHERE food_id = '{food_id}';
                             '''))
            con.commit()
        return