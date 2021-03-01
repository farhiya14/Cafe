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

# A cursor is an object that represents a DB cursor, which is used to manage the context of a fetch operation.
cursor = connection.cursor()

# Add code here to insert a new record
mycursor = connection.cursor()

def insert_to_table(table,name, other):

    # other = price or number in products or couriers

    sql = "INSERT INTO {} ({}, {}) VALUES (%s, %s)".format(table,name,other)
    val = ("{}".format(name) , "{}".format(other))
    mycursor.execute(sql, val)

    mycursor.commit()
    connection.commit()
    cursor.close()
    connection.close()

def insert_order_to_table(name, address, number, courier, status, items):
    sql = "INSERT INTO Orders ({}, {}, {}, {}, {}, {}) VALUES (%s, %s, %s, %s, %s, %s)".format(name, address, number, courier, status, items)
    val = ("{}".format(name), "{}".format(address), "{}".format(number), "{}".format(courier), "{}".format(status), "{}".format(items))
    mycursor.execute(sql, val)

    mycursor.commit()
    connection.commit()
    cursor.close()
    connection.close()

def remove_from_table(table, column_name, id_num):
    
    # "DELETE FROM table WHERE column name = 'contents '"
    #eg "DELETE FROM products WHERE id = '3'"
    # make sure to fetch id number first

    sql = "DELETE FROM {} WHERE {} = '{}'".format(table, column_name, id_num)
    mycursor.execute(sql)

    mycursor.commit()
    connection.commit()
    cursor.close()
    connection.close()

def update_to_table(table, column_name, new, old):

    # individual cell updates
    # fetch old/current info

    sql = "UPDATE {} SET {} = '{}' WHERE {} = '{}'".format(table, column_name, new, column_name, old)

    mycursor.execute(sql)
    
    mycursor.commit()
    connection.commit()
    cursor.close()
    connection.close()




mycursor.commit()
connection.commit()
cursor.close()
connection.close()
