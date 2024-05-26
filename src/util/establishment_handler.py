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
        print('goes to update_establishment')
        with self.db_connection.connect() as con:
            con.execute(text(f'''
                            UPDATE establishment 
                            SET establishment_name = '{establishment_name}'
                            WHERE establishment_id = {establishment_id};
                        '''))
            con.commit()
        return