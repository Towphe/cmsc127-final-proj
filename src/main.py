import mariadb
import sys
from util.repository import Repository

repository = Repository()

is_running = True
while(is_running):
    opt = int(input())
    match opt:
        case 0:
            print("...Closing...")
            is_running = False