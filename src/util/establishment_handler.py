import mariadb
import sys
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sqlalchemy.sql import text

class EstablishmentHandler:
    def __init__(self, db_connection):
        self.db_connection = db_connection
    
    def get_establishments(self):
        establishments = pd.read_sql('SELECT * FROM establishment', con=self.db_connection)
        return establishments
    
    def add_establishment(self, added_by, establishment_name):
        with self.db_connection.connect() as con:
            con.execute(text(f"INSERT INTO establishment (added_by, establishment_name) VALUES ('{added_by}', '{establishment_name}') "))
            con.commit()
        return
    
    def remove_establishment(self, establishment_id):
        with self.db_connection.connect() as con:
            con.execute(text(f'''
                             DELETE FROM establishment
                             WHERE establishment_id = {establishment_id};
                             '''))
            con.commit()
        return
    
    def update_establishment(self, establishment_id, establishment_name):
        with self.db_connection.connect() as con:
            con.execute(text(f'''
                            UPDATE establishment 
                            SET establishment_name = '{establishment_name}'
                            WHERE establishment_id = {establishment_id};
                        '''))
            con.commit()
        return
    
    def create_establishment_review(self, establishment_id:int, reviewer:str, content:str, rating:float):
        with self.db_connection.connect() as con:
            con.execute(text(f'''
                            INSERT INTO establishment_review (establishment_id, reviewer_username, content, rating)
                            VALUES ({establishment_id}, '{reviewer}', '{content}', '{rating}');
                        '''))
            con.commit()
            con.execute(text(f'''
                            UPDATE establishment 
                            SET average_rating = (
                                SELECT AVG(rating) 
                                FROM establishment_review 
                                WHERE establishment_id = '{establishment_id}')
                            WHERE establishment_id = '{establishment_id}';
                             '''))  # this leads to faster reads
            con.commit()
        return
    
    def get_establishment_reviews(self, establishment_id):
        establishment_reviews = pd.read_sql(f"SELECT * FROM establishment_review WHERE establishment_id = '{establishment_id}'", con=self.db_connection)
        return establishment_reviews
    
    def update_establishment_review(self, establishment_id:int, content:str, rating:float):
        with self.db_connection.connect() as con:
            con.execute(text(f'''
                            UPDATE establishment_review 
                            SET (content = '{content}', rating = '{rating}') 
                            WHERE review_id = "review_id";
                        '''))
            con.commit()
            con.execute(text(f'''
                            UPDATE establishment 
                            SET average_rating = (
                                SELECT AVG(rating) 
                                FROM establishment_review 
                                WHERE establishment_id = '{establishment_id}')
                            WHERE establishment_id = '{establishment_id}';
                             '''))  # this leads to faster reads
            con.commit()
        return
    
    def delete_establishment_Review(self, review_id:int, establishment_id:int):
        with self.db_connection.connect() as con:
            con.execute(text(f'''
                            DELETE FROM establishment_review 
                            WHERE review_id = '{review_id}';
                        '''))
            con.commit()
            con.execute(text(f'''
                            UPDATE establishment 
                            SET average_rating = (
                                SELECT AVG(rating) 
                                FROM establishment_review 
                                WHERE establishment_id = '{establishment_id}')
                            WHERE establishment_id = '{establishment_id}';
                             '''))
            con.commit()
        return