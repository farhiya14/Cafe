from dotenv import load_dotenv
import pymysql
import csv
import os

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

# ---------------------Main menu-----------------------------------------------------------
def courier_menu():

    print("\nCourier Menu\n")
    print("To return to Main Menu enter         0")
    print("To view couriers enter               1")
    print("To add a new courier enter           2")
    print("To update courier enter              3")
    print("To remove a courier enter            4")
    try:
        input3 = int(input("Where to: "))
        if input3 == 0:
            print("\nReturn to Main Menu\n")
            os.system('clear')
            import new_app
            return new_app.main_menu()
        elif input3 == 1:
            load_file_couriers()
            return courier_menu()
        elif input3 == 2:
            return create_new_courier()
        elif input3 == 3:
            return navigator(input3)
        elif input3 == 4:
            return navigator(input3)
        else:
            print("\nInvalid input!\nReturning to courier menu")
            return courier_menu()
    except ValueError:
        print("\nInvalid input!\nReturning to courier menu")
        return courier_menu()
    os.system('clear')

# ------------------Create a new courier-------------------------------------------
def new_name():

    new_courier_name = input("\nEnter courier name: ")
    new_courier_name = new_courier_name.title()

    while new_courier_name == "":
        print("\nDo not leave blank\n")
        new_courier_name = input("Enter new name: ")
        new_courier_name = new_courier_name.title()

    confirm = input(
        "Is this correct '{}'? Enter 0 for yes and 1 for no: ".format(new_courier_name))

    while confirm == "" or confirm.isdigit() == False:
        print("please enter valid response")
        confirm = input(
            "Is this correct '{}'? Enter 0 for yes and 1 for no: ".format(new_courier_name))

    confirm = int(confirm)

    if confirm == 0:
        pass
        # return new_courier_name
    elif confirm == 1:
        return new_name()
    else:
        return new_name()

    return new_courier_name

def new_number():

    new_courier_number = input("Enter phone number: ")

    while new_courier_number == "" or len(new_courier_number) != 11 or new_courier_number.isdigit() == False:
        print("Enter a valid phone number\n")
        new_courier_number = input("Enter phone number: ")

    confirm = input("Is this correct '{}'? Enter 0 for yes and 1 for no: ".format(
        new_courier_number))

    while confirm == "" or confirm.isdigit() == False:
        print("please enter valid response")
        confirm = input(
            "Is this correct '{}'? Enter 0 for yes and 1 for no: ".format(new_courier_number))

    confirm = int(confirm)

    if confirm == 0:
        return new_courier_number
    elif confirm == 1:
        return new_number()
    else:
        return new_number()

    return new_courier_number

def courier_id():

    couriers = load_file_couriers()

    try:

        last_courier_in_list = couriers[-1]
        # print(last_courier_in_list)
        # print(last_courier_in_list["id"])

        for courier in couriers:
            if int(courier["id"]) <= int(last_courier_in_list["id"]):
                continue

        new_id = int(last_courier_in_list["id"]) + 1
        return new_id

    except IndexError:
        return 1

def add_courier_to_list(new_id, name, number):

    couriers = load_file_couriers()

    new_courier = { "id": new_id,
                    "name": name,
                    "number": number}

    insert_to_table(new_id, name, number)

    couriers.append(new_courier)
    add_new_courier_file(new_courier)

    return new_courier

def create_new_courier():
    os.system('clear')

    print("\nNew Courier\n")

    add_courier_to_list(courier_id(), new_name(), new_number())

    os.system('clear')
    return courier_menu()

# --------------------Get courier----------------------------------------------------------------
def navigator(input3):

    try:
        if input3 == 3:
            return update_courier()
        elif input3 == 4:
            return removal_of_courier()

    except ValueError:
        print("\nInvalid input\n")
        return courier_menu()

def get1():

    load_file_couriers()

    selected = input("select courier or 0 to cancel: ")

    return selected

def get_courier():

    selected = get1()

    try:
        selected = int(selected)

        if selected == 0:
            print("\nReturning to Courier menu\n")
            return courier_menu()

        else:
            selected = selected - 1
            selected_courier = couriers[selected]
            print(selected_courier)
            return selected_courier

    except IndexError:
        print("{} is not in the list".format(selected + 1))
        return get_courier()
    except ValueError:
        print("{} is not in the list".format(selected + 1))
        return get_courier()

# ---------------------Update a courier--------------------------------------------------
def update_courier():

    selected= get_courier()

    update_name(selected)

    update_number(selected)

    save_updated_couriers()

    os.system('clear')

    print("Database has been successfully updated\n")

    return courier_menu()

def update_name(select):

    print("\nUpdate name")
    new_name = input("Enter replacment or press enter key to keep same: ")
    new_name = new_name.title()

    the_id= select["id"]

    if new_name != "":
        select["name"] = new_name

        # cursor = connection.cursor()
        # mycursor = connection.cursor()

        sql = "UPDATE Couriers SET name = %s WHERE id = %s"
        val = (new_name, the_id)

        cursor.execute(sql,val)
        connection.commit()
        # cursor.close()
        # connection.close()

def update_number(selected):

    print("\nUpdate phone number ")
    new_number = input("Enter replacment or press enter key to keep same: ")
    new_number.rstrip()

    the_id = selected["id"]

    if new_number != "":
        while len(new_number) != 11 or new_number.isdigit() == False:
            print("Enter a valid phone number\n")
            new_number = input(
                "Enter replacment or press enter key to keep same: ")

        selected["number"] = new_number

        sql = "UPDATE Couriers SET number = %s WHERE id = %s"
        val = (new_number, the_id)

        cursor.execute(sql,val)
        connection.commit()
        cursor.close()
        connection.close()

#----------------------Remove a courier----------------------------------------------------
def removal_of_courier():

    selected = get_courier()

    the_id = selected["id"]

    remove_from_database(the_id)

    couriers.remove(selected)
    save_updated_couriers()
    print("\nsuccessfully removed\n")

    os.system('clear')

    return courier_menu()

#----------------------File handling-------------------------------------------------------
def load_file_couriers():
    with open("couriers list.csv", mode='r+') as file:
        reader = csv.DictReader(file, delimiter=',')
        print("\nCouriers list:")
        global couriers
        couriers = []
        for i, row in enumerate(reader):
            i += 1
            print(i, row)
            couriers.append(row)
        return couriers

def add_new_courier_file(new_courier):
    with open("couriers list.csv", mode='a') as file:
        writer = csv.DictWriter(file, delimiter=',', fieldnames=[
                                "id", "name", "number"])
        writer.writerow(new_courier)

def save_updated_couriers():
    with open("couriers list.csv", mode='w') as file:
        writer = csv.DictWriter(file, delimiter=',', fieldnames=[
                                "id", "name", "number"])
        writer.writeheader()
        # couriers = sorted(orders, key=lambda i: i["id"])
        for courier in couriers:
            writer.writerow(courier)

def checking_file_existance_couriers():
    import os.path

    if os.path.isfile("couriers list.csv"):
        return load_file_couriers()
    else:
        save_updated_couriers()
        return load_file_couriers()

#------------------------Database connections--------------------------------------------------
def get_couriers_from_database():
    sql = 'SELECT * FROM Couriers'

    mycursor.execute(sql)

    result = mycursor.fetchall()

    couriers = []
    for courier in result:
        couriers.appened(courier)
        print(courier)
    
    # mycursor.commit()
    connection.commit()
    cursor.close()
    connection.close()

    return couriers

def insert_to_table(new_id, name, other):

    sql = "INSERT INTO Couriers (id,name,number) VALUES (%s,%s,%s)"
    val = (new_id,name,other)

    mycursor.execute(sql, val)

    # mycursor.commit()
    connection.commit()
    cursor.close()
    connection.close()

def update_database(column_name, new, the_id):

    sql = "UPDATE Couriers SET %s = %s WHERE id = %s"
    val = (column_name, new, the_id)

    cursor.execute(sql,val)
    connection.commit()
    cursor.close()
    connection.close()

    print("Database has been successfully updated")

def remove_from_database(the_id):
    sql = "DELETE FROM Couriers WHERE id = %s"
    val = the_id

    cursor.execute(sql,val)
    connection.commit()
    cursor.close()
    connection.close()

    print("Database has been successfully updated")

