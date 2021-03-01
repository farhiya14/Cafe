import pymysql
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

# Establish a database connection
connection = pymysql.connect(
    host,
    user,
    password,
    database
)

# A cursor is an object that represents a DB cursor,
# which is used to manage the context of a fetch operation.

# Execute SQL query

def update_table(column_name, new, old):

    cursor = connection.cursor()

    cursor.execute('UPDATE Couriers SET {} = {} WHERE {}  = {}'.format(column_name, column_name, new, old))


    cursor.commit()


    cursor.close()
    print("done")



# Closes the connection to the DB, make sure you ALWAYS do this
connection.close()
