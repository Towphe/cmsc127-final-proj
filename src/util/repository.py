import mariadb
import sys
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from util.food_handler import FoodHandler
from util.establishment_handler import EstablishmentHandler
from util.reports_handler import ReportsHandler
from util.user_handler import UserHandler
import os
from dotenv import load_dotenv

load_dotenv()

class Repository:
    def __init__(self):
        db_connection_str = os.getenv("DB_KEY")
        db_connection = create_engine(db_connection_str)
        self.Food = FoodHandler(db_connection)
        self.Establishment = EstablishmentHandler(db_connection)
        self.Reports = ReportsHandler(db_connection)
        self.Users = UserHandler(db_connection)