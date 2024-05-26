import mariadb
import sys
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sqlalchemy.sql import text

class FoodHandler:
    def __init__(self, db_connection):
        self.db_connection = db_connection
    
    def get_establishments(self):
        establishments = pd.read_sql('SELECT * FROM food', con=self.db_connection)
        return establishments
    
    def add_food(self, food_name, price):
        with self.db_connection.connect() as con:
            con.execute(text(f"INSERT INTO food (food_name, price) VALUES ('{food_name}', '{price}') "))
            con.commit()
        return
    
    def remove_food(self, food_id):
        with self.db_connection.connect() as con:
            con.execute(f"DELETE FROM food WHERE food_id = {food_id}")
            con.commit()
        return
    
    def update_food(self, food_id, food_name):
        with self.db_connection.connect() as con:
            con.execute(f'''
                            UPDATE food 
                            SET food_name = {food_name}
                            WHERE food_id = {food_id}
                        ''')
            con.commit()
        return