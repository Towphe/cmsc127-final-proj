import pandas as pd
import numpy as np
from sqlalchemy.sql import text

class UserHandler():
    def __init__(self, db_connection):
        self.db_connection = db_connection
    
    def sign_in(self, username:str, password:str):
        user = pd.read_sql(f"SELECT * FROM user WHERE username = '{username}'", con=self.db_connection)

        if user.shape[0] == 0:
            # none found
            return (False, 'NonExistent')
        if password != user.iloc[0].password:
            return (False, 'WrongPassword')
        return (True, 'Matched')

    def sign_up(self, username:str, password:str):
        user = pd.read_sql(f"SELECT * FROM user WHERE username = '{username}'", con=self.db_connection)
        if user.shape[0] != 0:
            return (False, 'UsernameTaken')
        with self.db_connection.connect() as con:
            con.execute(text(f'''
                            INSERT INTO user (username, password, type)
                            VALUES ('{username}', '{password}', 'USER');
                             '''))
            con.commit()
        return (True, 'Success')