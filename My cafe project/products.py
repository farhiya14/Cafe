import csv
import os
import pymysql
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

# ----------------------Main menu--------------------------------------------------------------
def product_menu():
    print("\nProduct Menu\n")
    print("To return to Main Menu enter     0")
    print("To view products enter           1")
    print("To add a new product enter       2")
    print("To add a update product enter    3")
    print("To remove a product enter        4")
    input2 = int(input("Where to: "))
    try:
        if input2 == 0:
            print("\nReturn to Main Menu\n")
            os.system('clear')
            import new_app
            return new_app.main_menu()
        elif input2 == 1:
            load_file_products()
            return product_menu()
        elif input2 == 2:
            return create_new_product()
        elif input2 == 3:
            return navigator(input2)
        elif input2 == 4:
            return navigator(input2)
        else:
            print("\nInvalid input! Returning to product menu")
            return product_menu()
    except ValueError:
        print("\nInvalid input!\nReturning to product menu")
        return product_menu()
    os.system('clear')

# -------------------------Create a new product------------------------------------------------
def create_new_product():
    os.system('clear')

    print("\nAdd New Product\n")

    # load_file_products()

    add_product_to_list(product_id(), new_name(), new_price())

    os.system('clear')

    return product_menu()

def new_name():

    new_product_name = input("Enter product name: ")
    new_product_name = new_product_name.title()

    while new_product_name == "":
        print("\nDo not leave blank\n")
        new_product_name = input("Enter product name: ")
        new_product_name = new_product_name.title()

    confirm = input(
        "Is this correct '{}'? Enter 0 for yes and 1 for no: ".format(new_product_name))

    while confirm == "" or confirm.isdigit() == False:
        print("please enter valid response")
        confirm = input(
            "Is this correct '{}'? Enter 0 for yes and 1 for no: ".format(new_product_name))

    confirm = int(confirm)

    if confirm == 0:
        pass
    elif confirm == 1:
        return new_name()
    else:
        return new_name()

    return new_product_name

def new_price():
    try:

        new_price = float(
            input("Enter product price "))
        return new_price

    except ValueError:
        print("please enter a valid input")
        return new_price()

def product_id():
    products = load_file_products()
    try:

        last_product_in_list = products[-1]
        # print(last_product_in_list)
        # print(last_product_in_list["id"])

        for product in products:
            if int(product["id"]) <= int(last_product_in_list["id"]):
                continue

        new_id = int(last_product_in_list["id"]) + 1
        return new_id

    except IndexError:
        return 1

def add_product_to_list(new_id, name, price):

    new_product = {"id": new_id,
                    "name": name,
                    "price": price}

    insert_to_table(new_id, name, price)

    products.append(new_product)

    add_new_product_file(new_product)

    return new_product

# -----------------------Get product----------------------------------------------------------
def navigator(input2):

    try:
        if input2 == 3:
            return update_products()
        elif input2 == 4:
            return removal_of_product()

    except ValueError:
        print("\nInvalid input\n")
        return product_menu()

def get_product():

    selected = get2()

    try:
        selected = int(selected)

        if selected == 0:
            print("\nReturning to Product menu\n")
            return product_menu()

        else:
            selected = selected - 1
            selected_product = products[selected]
            print(selected_product)
            return selected_product

    except IndexError:
        print("{} is not in the list".format(selected + 1))
        return get_product()
    finally:
        return selected_product

def get2():
    load_file_products()

    selected = input("select product or 0 to cancel: ")

    return selected

# -----------------------Update a product -----------------------------------------------------
def update_products():
    selected = get_product()

    update_name(selected)

    update_price(selected)

    save_updated_products()

    os.system('clear')

    return product_menu()

def update_name(select):

    print("\nUpdate name")
    new_name = input("Enter replacment or press enter key to keep same: ")
    new_name = new_name.title()

    the_id = select["id"]

    if new_name != "":

        select["name"] = new_name

        cursor = connection.cursor()
        mycursor = connection.cursor()

        sql = "UPDATE Products SET name = %s WHERE id = %s"
        val = (new_name, the_id)

        cursor.execute(sql,val)
        connection.commit()
        # cursor.close()
        # connection.close()

        # print("Database has been successfully updated")

def update_price(selected):

    print("\nUpdate price ")

    new_price = input("Enter replacment or press enter key to keep same: ")

    the_id = selected["id"]

    if new_price != "":
        try:
            new_price = float(new_price)
            selected["price"] = new_price

            # cursor = connection.cursor()
            # mycursor = connection.cursor()

            sql = "UPDATE Products SET price = %s WHERE id = %s"
            val = (new_price, the_id)

            cursor.execute(sql,val)
            connection.commit()
            cursor.close()
            connection.close()

            print("Database has been successfully updated")

        except ValueError:
            print("Enter a valid price\n")
            return update_price(selected)
        # except:
        #     print("other error?")

# ----------------------Removing a product ----------------------------------------------------
def removal_of_product():
    selected = get_product()

    the_id = selected["id"]

    remove_from_database(the_id)

    products.remove(selected)

    save_updated_products()
    print("\nsuccessfully removed\n")

    os.system('clear')

    return product_menu()

# ---------------------File handling-----------------------------------------------------------
def load_file_products():
    with open("products list.csv", mode='r+') as file:
        reader = csv.DictReader(file, delimiter=',')
        print("\nProducts list:")
        global products
        products = []
        for i, row in enumerate(reader):
            i += 1
            print(i, row)
            products.append(row)
    return products

def add_new_product_file(new_product):
    with open("products list.csv", mode='a') as file:
        writer = csv.DictWriter(file, delimiter=',', fieldnames=[
                                "id", "name", "price"])
        writer.writerow(new_product)

def save_updated_products():
    with open("products list.csv", mode='w') as file:
        writer = csv.DictWriter(file, delimiter=',', fieldnames=[
                                "id", "name", "price"])
        writer.writeheader()
        for product in products:
            writer.writerow(product)

def checking_file_existance_products():
    import os.path

    if os.path.isfile("products list.csv"):
        return load_file_products()
    else:
        save_updated_products()
        load_file_products()

def products_list():
    with open("products list.csv", mode='r+') as file:
        reader = csv.DictReader(file, delimiter=',')
        products = []
        for i, row in enumerate(reader):
            i += 1
            products.append(row)
    return products

#------------------------Database connections--------------------------------------------------
def get_products_from_database():
    sql = 'SELECT * FROM Products'

    mycursor.execute(sql)

    result = mycursor.fetchall()

    products = []

    for product in result:
        products.appened(product)
        print(product)
    
    # mycursor.commit()
    connection.commit()
    cursor.close()
    connection.close()

    return products

def insert_to_table(new_id, name, other):

    cursor = connection.cursor()

    mycursor = connection.cursor()

    sql = "INSERT INTO Products (id,name,price) VALUES (%s,%s,%s)"
    val = (new_id,name,other)

    mycursor.execute(sql, val)

    # mycursor.commit()
    connection.commit()
    cursor.close()
    connection.close()

def update_database(column_name, new, the_id):

    sql = "UPDATE Products SET %s = %s WHERE id = %s"
    val = (column_name, new, the_id)

    cursor.execute(sql,val)
    connection.commit()
    cursor.close()
    connection.close()

    print("Database has been successfully updated")

def remove_from_database(the_id):

    cursor = connection.cursor()
    mycursor = connection.cursor()
    
    sql = "DELETE FROM Products WHERE id = %s"
    val = the_id

    mycursor.execute(sql, val)
    
    connection.commit()
    cursor.close()
    connection.close()

    print("Database has been successfully updated")

# checking_file_existance_products()

products_listed = products_list()

print(products_listed)