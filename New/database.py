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

mycursor = connection.cursor()

def insert_to_table(table, the_id, name, other):

    # other = price or number in products or couriers

    sql = "INSERT INTO {} ({}, {}, {}) VALUES (%s, %s, %s)".format(table, the_id, name, other)
    val = ("{}".format(the_id), "{}".format(name), "{}".format(other))
    mycursor.execute(sql, val)


    mycursor.commit()
    connection.commit()
    cursor.close()
    connection.close()

    print("Database has been successfully updated")

def insert_order_to_table(name, address, number, courier, status, items):
    sql = "INSERT INTO Orders ({}, {}, {}, {}, {}, {}) VALUES (%s, %s, %s, %s, %s, %s)".format(
        name, address, number, courier, status, items)
    val = ("{}".format(name), "{}".format(address), "{}".format(number),
        "{}".format(courier), "{}".format(status), "{}".format(items))
    
    mycursor.execute(sql, val)

    mycursor.commit()
    connection.commit()
    cursor.close()
    connection.close()

    print("Database has been successfully updated")

def remove_from_table(table, id_num):

    # "DELETE FROM table WHERE column name = 'contents '"
    #eg "DELETE FROM products WHERE id = '3'"
    # make sure to fetch id number first

    sql = "DELETE FROM {} WHERE id = '{}'".format(table, id_num)
    mycursor.execute(sql)

    mycursor.commit()
    connection.commit()
    cursor.close()
    connection.close()

    print("Database has been successfully updated")

def update_to_table(table, column_name, new, column_name2, old):

    # individual cell updates
    # fetch old/current info
    #eg: UPDATE Orders SET status = 'delivered' WHERE id = 4
    #eg: ""UPDATE Product SET price = '1.25' WHERE price = 0.95""


    sql = "UPDATE {} SET {} = '{}' WHERE {} = '{}'".format(
        table, column_name, new, column_name2, old)

    mycursor.execute(sql)

    mycursor.commit()
    connection.commit()
    cursor.close()
    connection.close()

    print("Database has been successfully updated")

# from database import insert_to_table
# insert_order_to_table(Products, name, price)

# connection.commit()
# cursor.close()
# connection.close()


