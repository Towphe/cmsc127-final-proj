
# CMSC 127 Final Project

This repository contains our group's final project, a food and restaurant review system, written in Python and TKinter, with data persistence in MariaDB.

## Running the Program

To run the program, make sure to create the tables detailed in the table creation file in the root directory of the repository. 

Also, create a `.env` file on the root directory, containing a variable `DB_KEY` containing your database credentials in the following format:

    	mariadb+pymysql://<username>:<password>@<server/domain>:<port>/<db_name>

Then, run the following:

    $	bash run.sh

This automatically creates a virtual environment, installs the packages used, and runs the program.