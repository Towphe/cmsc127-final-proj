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
    
    def find_establishment_with_key(self, establishment_name:str):
        establishments = pd.read_sql(f"SELECT * FROM establishment WHERE establishment_name LIKE '%%{establishment_name}%%'", con=self.db_connection)
        return establishments
    
    def find_establishment_by_id(self, establishment_id:int):
        establishment = pd.read_sql(f'SELECT * FROM establishment WHERE establishment_id = {establishment_id} ', con=self.db_connection)
        return establishment.iloc[0]
    
    def add_establishment(self, added_by:str, establishment_name:str):
        with self.db_connection.connect() as con:
            con.execute(text(f"INSERT INTO establishment (added_by, establishment_name) VALUES ('{added_by}', '{establishment_name}');"))
            con.commit()
        return
    
    def remove_establishment(self, establishment_id:int):
        with self.db_connection.connect() as con:
            con.execute(text(f'''
                            DELETE FROM establishment
                            WHERE establishment_id = {establishment_id};
                            '''))
            con.commit()
        return
    
    def update_establishment(self, establishment_id:int, establishment_name:str):
        with self.db_connection.connect() as con:
            con.execute(text(f'''
                            UPDATE establishment 
                            SET establishment_name = '{establishment_name}',
                                average_rating = (SELECT average_rating FROM establishment WHERE establishment_id = {establishment_id})
                            WHERE establishment_id = {establishment_id};
                        '''))
            con.commit()
        return
    
    def create_establishment_review(self, establishment_id:int, reviewer:str, content:str, rating:float):
        with self.db_connection.connect() as con:
            con.execute(text(f'''
                            INSERT INTO establishment_review (establishment_id, reviewer_username, content, rating)
                            VALUES ({establishment_id}, '{reviewer}', '{content}', {rating});
                        '''))
            con.commit()
            con.execute(text(f'''
                            UPDATE establishment 
                            SET average_rating = (
                                SELECT AVG(rating) 
                                FROM establishment_review 
                                WHERE establishment_id = {establishment_id})
                            WHERE establishment_id = {establishment_id};
                             '''))  # this leads to faster reads
            con.commit()
        return
    
    def get_establishment_reviews(self, establishment_id:int):
        establishment_reviews = pd.read_sql(f"SELECT * FROM establishment_review WHERE establishment_id = '{establishment_id}'", con=self.db_connection)
        return establishment_reviews
    
    def get_establishment_review_by_id(self, review_id):
        establishment_review = pd.read_sql(f"SELECT * FROM establishment_review WHERE review_id = {review_id} ", con=self.db_connection)
        return establishment_review.iloc[0]

    def get_all_establishment_reviews(self):
        all_establishment_reviews = pd.read_sql(f"SELECT * FROM establishment_review", con=self.db_connection)
        return all_establishment_reviews
    
    def get_all_establishment_reviews_by(self, username:str):
        all_establishment_reviews = pd.read_sql(f"SELECT * FROM establishment_review WHERE reviewer_username='{username}'", con=self.db_connection)
        return all_establishment_reviews
    
    def update_establishment_review(self, review_id:int, establishment_id:int, content:str, rating:float):
        with self.db_connection.connect() as con:
            con.execute(text(f'''
                            UPDATE establishment_review 
                            SET content = '{content}', rating = {rating}
                            WHERE review_id = {review_id};
                        '''))
            con.commit()
            con.execute(text(f'''
                            UPDATE establishment 
                            SET average_rating = (
                                SELECT AVG(rating) 
                                FROM establishment_review 
                                WHERE establishment_id = {establishment_id})
                            WHERE establishment_id = {establishment_id};
                             '''))  # this leads to faster reads
            con.commit()
        return
    
    def delete_establishment_Review(self, review_id:int, establishment_id:int):
        with self.db_connection.connect() as con:
            con.execute(text(f'''
                            DELETE FROM establishment_review 
                            WHERE review_id = {review_id};
                        '''))
            con.commit()
            con.execute(text(f'''
                            UPDATE establishment 
                            SET average_rating = (
                                SELECT AVG(rating) 
                                FROM establishment_review 
                                WHERE establishment_id = {establishment_id})
                            WHERE establishment_id = {establishment_id};
                             '''))
            con.commit()
        return