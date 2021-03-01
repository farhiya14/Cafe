from couriers import load_file_couriers
from products import load_file_products

import os
import csv

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

#---------------------Order menu-----------------------------------------------------------------
def order_menu():
    # os.system('clear')

    print("\nOrder Menu\n")
    print("To return to Main Menu enter         0")
    print("To view orders enter                 1")
    print("To add a new order enter             2")
    print("To add a update order status enter   3")
    print("To update an order enter             4")
    print("To remove a order enter              5")
    try:
        input4 = int(input("Where to: "))

        if input4 == 0:
            print("\nReturn to Main Menu\n")
            os.system('clear')
            from new_app import main_menu
            return main_menu()
        elif input4 == 1:
            load_file_orders()
            return order_menu()
        elif input4 == 2:
            print("\nNew Order:\n")
            return create_new_order()
        elif input4 == 3:
            print("\nUpdate Order Status:\n")
            return navigator(input4)
        elif input4 == 4:
            print("\nUpdate an Order:\n")
            return navigator(input4)
        elif input4 == 5:
            print("\nRemove an order\n")
            return navigator(input4)
        else:
            print("Invalid input\nTry again")
            return order_menu()
    except ValueError:
        print("\nInvalid Input_menu\n")
        return order_menu()

    os.system('clear')

#----------------------Add new order--------------------------------------------------------------
def create_new_order():
    os.system('clear')

    new_order = add_new_order(ord_id(), new_customer_name(), new_address(),
    new_cust_number(),add_courier_new_order(),product_selection())

    add_new_order_file(new_order)

    save_updated_orders()

    print("\nOrder has been added\n")

    os.system('clear')

    return order_menu()

def ord_id():

    try:

        last_order_in_list = orders[-1]
        # print(last_order_in_list)
        # print(last_order_in_list["id"])

        for order in orders:
            if int(order["id"]) <= int(last_order_in_list["id"]):
                continue

        new_id = int(last_order_in_list["id"]) + 1
        return new_id

    except IndexError:
        return 1

def new_customer_name():
    name = str(input("Customer name: "))
    name = name.title()

    while name == "":
        print("Do not leave blank\n")
        name = str(input("Customer name: "))
        name = name.title()

    return name

def new_address():
    address = str(input("Customer address: "))
    address = address.title()

    while address == "":
        print("Do not leave blank\n")
        address = str(input("Customer address: "))
        address = address.title()

    return address

def new_cust_number():
    phone_num = input("Customer phone number: ")

    while phone_num == "" or len(phone_num) != 11 or phone_num.isdigit() == False:
        print("Enter a valid phone number\n")
        phone_num = input("Customer phone number: ")

    return phone_num

def couriers_list():
    with open("couriers list.csv", mode='r') as file:
        reader = csv.DictReader(file, delimiter=',')
        global couriers
        couriers = []
        for i, row in enumerate(reader):
            i += 1
            couriers.append(row)
    return couriers

def add_courier_new_order():
    load_file_couriers()

    couriers = couriers_list()

    picked_courier = input("select a courier from the list: ")

    try:
        picked_courier = int(picked_courier)
        index = couriers.index(courier_selection(picked_courier)) + 1
        print("\n",courier_selection(picked_courier))
        return index

    except ValueError:
        print("\nPlease select a number\n")
        return add_courier_new_order()
    except IndexError:
        print("\nPlease select from the list\n")
        return add_courier_new_order()

def is_integer(item):
    try:
        float(item)
    except ValueError:
        return False
    else:
        return float(item).is_integer()

def product_selection():
    products = load_file_products()

    selected_items = input(
        "\nPlease select products from list above, use comma(,) to seperate items or 0 to cancel: ")
    selected_items = selected_items.strip()

    if selected_items == '0':
        print("cancelling order")
        return order_menu()

    elif selected_items == "":
        print("\nDo not leave blank\nTry again")
        return product_selection()


    selected_products_dicts = []
    show = []

    ordered_products = (selected_items.split(","))

    try:
        for item in ordered_products:
            if is_integer(item) == True:
                item = int(item)
                show.append(item)
                selected_products_dicts.append(products[item-1])
                continue

            else:
                print(
                    "'{}' is not a valid input and has not been added to list".format(item))
                continue
        
        new_3 = ""

        for item in show:
            new_3 = new_3 + str(item) + ","

        return new_3[:-1]

    except IndexError:
        print("\nIndex Error. Select a valid inputs\n")
        print("'{}' is not valid input".format((item)))
        return product_selection()

    except ValueError:
        print("'{}' is not a valid input and has not been added to list".format(item))
        return product_selection()

def add_new_order(o_id,name,address,number,courier,items):

    status = "preparing"

    new_order = {   "id": o_id,
                    "name": name,
                    "address": address,
                    "number": number,
                    "courier": courier,
                    "status": status,
                    "items": items
                    }

    insert_order_to_table(o_id, name, address, number, courier, status, items)

    orders.append(new_order)

    return new_order

#-------------------------Navigators-------------------------------------------------------
def navigator(input4):
    try:
        if input4 == 3:
            return only_update_status()
        elif input4 == 4:
            return update_order()
        elif input4 == 5:
            return remove_order()
    except ValueError:
        print("\nInvalid input_get_order\n")
        return order_menu()

def get3():
    load_file_orders()

    selected = input("select order or 0 to cancel: ")

    return selected

def get_order():

    selected = get3()

    if selected == "":
        return get3()

    try:
        selected = int(selected)

        if selected == 0:
            print("\nReturning to Order menu\n")
            return order_menu()

        selected -= 1

        # global selected_order

        selected_order = orders[selected]

        print("\n", selected_order, "\n")

        return selected_order

    except ValueError:
        print("Invalid entry\n")
        return get_order()

    except IndexError:
        print("\nInvalid entry\nTry again\n")
        return get_order()

#-------------------------Update status only---------------------------------------------------

def update_status_input():
    print("\n")
    print("Status':")
    print("1: preparing")
    print("2: on the way")
    print("3: delivered")

    try:
        new_status = int(input("\nSelect new status: "))
        return new_status

    except ValueError:
            print("not right2")
            return update_status_input()

def update_status(selected):

    new_status = update_status_input()

    if new_status == 1:
        status = "preparing"
    elif new_status == 2:
        status = "on the way"
    elif new_status == 3:
        status = "delivered"
    else:
        print("please enter from available list")
        return update_status_input()

    the_id = selected["id"]
    the_id = int(the_id)

    selected["status"] = status

    cursor = connection.cursor()
    mycursor = connection.cursor()

    sql = "UPDATE Orders SET status = %s WHERE id = %s"
    val = (status, the_id)

    cursor.execute(sql,val)
    connection.commit()
    cursor.close()
    connection.close()

    print("Database has been successfully updated")



    save_updated_orders()

    return new_status

def only_update_status():

    selected_order = get_order()

    update_status(selected_order)

    os.system('clear')

    return order_menu()

#-------------------------Update an order----------------------------------------------------
def to_update_status_1():
    print("\n")
    print("Status':")
    print("1: preparing")
    print("2: on the way")
    print("3: delivered")

    new_status = input("\nEnter replacment or press enter key to keep same: ")
    
    try:
        new_status = int(new_status)

        return new_status

    except ValueError:
        if new_status == "":
            return False
        else:
            print("please input a valid status\n")
            return to_update_status_1()

def to_update_status_2(chosen):

    new_status = to_update_status_1()

    if new_status == False:
        pass
    
    else:
        new_status = int(new_status)

        if new_status == 1:
            status = "preparing"
        elif new_status == 2:
            status = "on the way"
        elif new_status == 3:
            status = "delivered"
        else:
            print("please enter from available list")
            return to_update_status_1()
        
        the_id = chosen["id"]

        chosen["status"] = status

        sql = "UPDATE Orders SET status = %s WHERE id = %s"
        val = (status, the_id)

        cursor.execute(sql,val)
        connection.commit()
        # cursor.close()
        # connection.close()

        print("Database has been successfully updated")


        save_updated_orders()

def update_name(selected_order):

    print("\nUpdate name")
    new_name = input(
        "Enter replacment or press enter key to keep same: ")
    new_name = new_name.title()

    the_id = selected_order["id"]

    if new_name != "":
        selected_order["name"] = new_name

        cursor = connection.cursor()
        mycursor = connection.cursor()

        sql = "UPDATE Orders SET name = %s WHERE id = %s"
        val = (new_name, the_id)

        mycursor.execute(sql,val)
        connection.commit()
        # cursor.close()
        # connection.close()

        print("Database has been successfully updated")

def update_address(selected_order):
    print("\nUpdate address ")
    new_address = input(
        "Enter replacment or press enter key to keep same: ")
    
    the_id = selected_order["id"]

    if new_address != "":
        selected_order["address"] = new_address

        # cursor = connection.cursor()
        # mycursor = connection.cursor()

        sql = "UPDATE Orders SET address = %s WHERE id = %s"
        val = (new_address, the_id)

        cursor.execute(sql,val)
        connection.commit()
        # cursor.close()
        # connection.close()

        print("Database has been successfully updated")

def update_phone_number(selected_order):

    print("\nUpdate phone number ")
    new_number = input(
        "Enter replacment or press enter key to keep same: ")

    the_id = selected_order["id"]

    if new_number != "":
        while  len(new_number) != 11 or new_number.isdigit() == False:
            print("Enter a valid phone number\n")
            new_number = input(
                "Enter replacment or press enter key to keep same: ")
            if new_number == "":
                pass

        selected_order["number"] = new_number

        sql = "UPDATE Orders SET number = %s WHERE id = %s"
        val = (new_number, the_id)

        cursor.execute(sql,val)
        connection.commit()
        # cursor.close()
        # connection.close()

        print("Database has been successfully updated")

def update_courier(selected_order):
    load_file_couriers()

    couriers = couriers_list()

    picked_courier = input("Enter replacment or press enter key to keep same: ")

    try:

        if picked_courier != "":

            the_id = selected_order["id"]

            picked_courier = int(picked_courier)
            index = couriers.index(courier_selection(picked_courier)) + 1

            print(courier_selection(picked_courier))
            selected_order["courier"] = index

        sql = "UPDATE Orders SET courier = %s WHERE id = %s"
        val = (index, the_id)

        cursor.execute(sql,val)
        connection.commit()
        # cursor.close()
        # connection.close()

        print("Database has been successfully updated")


    except IndexError:
        print("wrong index")
        return update_courier(selected_order)

    except ValueError:
        if picked_courier == "":
            pass

def courier_selection(picked):

    try:
        picked = int(picked)
        picked -= 1
        return couriers[picked]

    except IndexError:
        print("idx error")
        return update_courier(picked)
    
    except ValueError:
        print("value erorr")
        return update_courier(picked)

#-------------------------Update items--------------------------------------------------------
def product_selection_input():

    load_file_products()

    selected_items = input(
        "\nPlease select products from list above, use comma(,) to seperate items or 0 to cancel: ")
    selected_items = selected_items.strip()

    if selected_items == '0':
        print("cancelling order")
        return order_menu()

    elif selected_items == "":
        # print("\norder has been successfuly updated")
        return False

    else:
        return selected_items

def products_list():
    with open("products list.csv", mode='r') as file:
        reader = csv.DictReader(file, delimiter=',')
        global products
        products = []
        for i, row in enumerate(reader):
            i += 1
            products.append(row)
    return products

def update_product_part_2():

    selected_items = product_selection_input()

    if selected_items == "" or selected_items == False:

        return False

    else:

        ordered_products = (selected_items.split(","))

        seperated_items = []

        products = products_list()
        # print(products)
        selected_products_dicts = []

        try:

            for item in ordered_products:
                if is_integer(item) == True:
                    item = int(item)
                    seperated_items.append(item)
                    selected_products_dicts.append(products[item-1])
                    continue

                else:
                    print(
                        "'{}' is not a valid input and has not been added to list".format(item))
                    continue
                
            # print(selected_products_dicts)
            return seperated_items

        except IndexError:
            print("\nIndex Error. Select a valid inputs\n")
            print("'{}' is not valid input".format((item)))
            return product_selection_input()

        except ValueError:
            print("'{}' is not a valid input and has not been added to list".format(item))
            return product_selection_input()

def update_product_part_3():
    items = update_product_part_2()

    if items != False:
        # print("at 3")
        output = ""

        for item in items:
            output = output + str(item) + ","

        # print(output[:-1])
        return output[:-1]

    else:
        print("now here")
        return False

def update_product_part_4(selected_order):

    if update_product_part_3() != False:

        the_id = selected_order["id"]

        new_items = update_product_part_3()
        selected_order["items"] = new_items


        sql = "UPDATE Orders SET items = %s WHERE id = %s"
        val = (new_items, the_id)

        cursor.execute(sql,val)
        connection.commit()
        cursor.close()
        connection.close()

        print("Database has been successfully updated")

def update_order():

    selected_order = get_order()

    update_name(selected_order)

    update_address(selected_order)

    update_phone_number(selected_order)

    update_courier(selected_order)

    update_product_part_4(selected_order)

    save_updated_orders()

    # os.system('clear')

    print("\norder has been successfuly updated")

    return order_menu()

#-------------------------Remove an order----------------------------------------------------
def remove_order():
    selected = get_order()

    the_id = selected["id"]

    remove_from_database(the_id)

    orders.remove(selected)

    save_updated_orders()
    print("\nsuccessfully removed\n")

    os.system('clear')

    return order_menu()

#-------------------------File handling-------------------------------------------------------
def load_file_orders():
    with open("orders list.csv", mode='r') as file:
        reader = csv.DictReader(file, delimiter=',')
        print("\nOrders list:")
        global orders
        orders = []
        for i, row in enumerate(reader):
            i += 1
            print(i, row)
            orders.append(row)
        return orders

def add_new_order_file(new_order):
    with open("orders list.csv", mode='a') as file:
        writer = csv.DictWriter(file, delimiter=',', fieldnames=[
                                "id", "name", "address", "number", "courier", "status", "items"])
        writer.writerow(new_order)

def save_updated_orders():
    with open("orders list.csv", mode='w') as file:
        writer = csv.DictWriter(file, delimiter=',', fieldnames=[
                                "id", "name", "address", "number", "courier", "status", "items"])
        writer.writeheader()
        new_orders_list = sorted(orders, key=lambda i: i["status"])
        for order in new_orders_list:
            writer.writerow(order)

def checking_file_existance_orders():
    import os.path

    if os.path.isfile("orders list.csv"):
        return load_file_orders()
    else:
        save_updated_orders()
        load_file_orders()

#------------------------Database connections--------------------------------------------------
def get_orders_from_database():
    sql = 'SELECT * FROM Orders'

    mycursor.execute(sql)

    result = mycursor.fetchall()

    orders = []
    for order in result:
        orders.append(order)
        print(order)

    # mycursor.commit()
    connection.commit()
    cursor.close()
    connection.close()

    return orders

def insert_order_to_table(o_id, name, address, number, courier, status, items):

    cursor = connection.cursor()
    mycursor = connection.cursor()

    sql = "INSERT INTO Orders (id, name, address, number, courier, status, items) VALUES (%s, %s, %s, %s, %s, %s, %s)"

    val = (ord_id, name, address, number, courier, status, items)

    mycursor.execute(sql, val)

    mycursor.commit()

    connection.commit()
    # cursor.close()
    connection.close()

    print("Database has been successfully updated")

def sort_by_status():

    cursor = connection.cursor()
    mycursor = connection.cursor()

    sql = "SELECT * FROM Order ORDER BY status"

    mycursor.execute(sql)

    connection.commit()
    cursor.close()
    connection.close()

def update_database(column_name, new, the_id):

    sql = "UPDATE Orders SET %s = %s WHERE id = %s"
    val = (column_name, new, the_id)

    cursor.execute(sql,val)
    connection.commit()
    cursor.close()
    connection.close()

    print("Database has been successfully updated")

def remove_from_database(the_id):
    sql = "DELETE FROM Orders WHERE id = %s"
    val = the_id

    cursor.execute(sql,val)
    connection.commit()
    cursor.close()
    connection.close()

    print("Database has been successfully updated")

