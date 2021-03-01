products = [{"name": "Coke",
             "price": 0.8,
             },
            {"name": "Water",
             "price": 0.65 }]#// float, }]

couriers = [{"name": "Jack",
             "phone number": "7418529966375"},
            {"name": "Tom",
             "phone number": "01478523695"}]


def main_menu():
    print("\nMain Menu")
    print("\nTo exit app enter 0")
    print("To go to Product Menu enter 1")
    print("To go to Courier Menu enter 2")
    print("To go to Order Menu enter 3")
    input1 = int(input("Where to: "))
    try:
        if input1 == 0:
            print("Exiting App")
            return quit()
        elif input1 == 1:
            return product_menu()
        elif input1 == 2:
            return courier_menu()
        elif input1 == 3:
            return order_menu()
        else:
            print("\nInvalid Input!")
            return main_menu()
    except ValueError:
        print("\nInvalid Input!")
        return main_menu()


def return_to_main_menu():
    print("\nReturn to Main Menu\n")
    return main_menu()


# --------------------------------------Product Menu----------------------------------------------------


def view_products_list():
    print("Products:\n")
    load_file_products()
    return product_menu()


def create_new_product():
    print("Products:\n")
    load_file_products()
    print("Create new product")
    global new_product
    new_product_name = input("Enter name of new product: ")
    new_product_name = new_product_name.title()
    new_product_price = float(input("Enter price of {}: " .format(new_product_name)))
    confirmation = int(
        input("Is this correct '{}', '{}'? Enter 0 for yes and 1 for no: ".format(new_product_name, new_product_price)))
    try:
        if confirmation == 0:
            if new_product_name in products:
                print("{} is already in the list.\nReturning to product menu".format(
                    new_product_name))
                return product_menu()
            else:
                print("{} has been added to product list\n".format(new_product_name))
                new_product = {"name": new_product_name,
                            "price": new_product_price}
                products.append(new_product)
                add_new_product_file()
                load_file_products()
                print("\nReturning to product menu")
                return product_menu()
        elif confirmation == 1:
            print("Returning to product menu")
            return product_menu()
        else:
            print("\nInvalid input!\nReturning to product menu")
            return product_menu()
    except ValueError:
        print("Invalid input!\nReturning to product menu")
        return product_menu()


def get_product():
    load_file_products()

    try:
        selected = int(input("select product or 0 to cancel: "))
        if selected == 0:
            print("\nReturning to Product menu\n")
            return product_menu()
        
        selected -= 1

        global selected_product

        selected_product = products[selected]
        print("\n",selected_product)

    except ValueError:
        print("Invalid entry\nReturning to Product menu")
        return product_menu()

    except IndexError:
        print("\nInvalid entry\nTry again")
        return product_menu()
    try:
        if input2 == 3:
            return update_products()
        elif input2 == 4:
            return removal_of_product()
    except ValueError:
        print("\nInvalid input\n")
        return product_menu()


def update_products():
    print("\nUpdate name")
    new_name = input(
        "Enter replacment or press enter key to keep same: ")
    new_name = new_name.title()
    if new_name != "":
        for product in products:
            if product == selected_product:
                selected_product["name"] = new_name

    print("\nUpdate price ")
    new_price = input(
        "Enter replacment or press enter key to keep same: ")

    if new_price != "":
        for product in products:
            if product == selected_product:
                selected_product["price"] = new_price
    
    save_updated_products()
    load_file_products()
    return product_menu()


def removal_of_product():

    try:
        products.remove(selected_product)
        save_updated_products()
        print("\nsuccessfully removed\n")
        load_file_products()
        return product_menu()
    except IndexError:
        print("Index error")


def product_menu():
    print("\nProduct Menu\n")
    print("To return to Main Menu enter 0")
    print("To view products enter 1")
    print("To add a new product enter 2")
    print("To add a update product enter 3")
    print("To remove a product enter 4")
    global input2
    input2 = int(input("Where to: "))
    try:
        if input2 == 0:
            return return_to_main_menu()
        elif input2 == 1:
            return view_products_list()
        elif input2 == 2:
            return create_new_product()
        elif input2 == 3:
            return get_product()
        elif input2 == 4:
            return get_product()
        else:
            print("\nInvalid input! Returning to product menu")
            return product_menu()
    except ValueError:
        print("\nInvalid input!\nReturning to product menu")
        return product_menu()


# ---------------------------------------Courier Menu----------------------------------------------------


def view_couriers_list():
    print("Couriers:\n")
    load_file_couriers()
    return courier_menu()


def create_new_courier():
    print("\nCourier list:\n")
    load_file_couriers()
    print("Create new courier")
    global new_courier
    new_courier_name = input("Enter name of new courier: ")
    new_courier_name = new_courier_name.title()
    new_courier_number = input("Enter {}'s phone number: ".format(new_courier_name))
    confirmation = int(
        input("Is this correct '{}', '{}'? Enter 0 for yes and 1 for no: ".format(new_courier_name,new_courier_number)))
    try:
        if confirmation == 0:
            if new_courier_name in couriers:
                print("{} is already in the list.\n\nReturning to product menu".format(
                    new_courier_name))
                return courier_menu()
            else:
                print("{} has been added to couriers list\n".format(new_courier_name))
                new_courier = {"name": new_courier_name, "phone number": new_courier_number}
                couriers.append(new_courier)
                add_new_courier_file()
                load_file_couriers()
                print("\nReturning to courier menu\n")
                return courier_menu()
        elif confirmation == 1:
            print("Returning to courier menu")
            return courier_menu()
        else:
            print("\nInvalid input!\nReturning to courier menu")
            return courier_menu()
    except ValueError:
        print("Invalid input!\nReturning to courier menu")
        return courier_menu()


def get_courier():
    
    for i, order in enumerate(orders):
        i += 1
        print(i, order)

    try:
        selected = int(input("select courier or 0 to cancel: "))
        if selected == 0:
            print("\nReturning to Courier menu\n")
            return courier_menu()

        selected -= 1

        if selected != (i -1) :
            print("\nNot in the list. Try again\n")
            return get_courier()

        global selected_courier

        selected_courier = couriers[selected]
        print("\n", selected_courier)

    except ValueError:
        print("Invalid entry\nReturning to Courier menu")
        return courier_menu()

    except IndexError:
        print("\nInvalid entry\nTry again")
        return courier_menu()
    try:
        if input3 == 3:
            return update_couriers()
        elif input3 == 4:
            return removal_of_courier()
    except ValueError:
        print("\nInvalid input\n")
        return courier_menu()


def update_couriers():
    print("\nUpdate name")
    new_name = input(
        "Enter replacment or press enter key to keep same: ")
    new_name = new_name.title()
    if new_name != "":
        for courier in couriers:
            if courier == selected_courier:
                selected_courier["name"] = new_name

    print("\nUpdate phone number ")
    new_number = input(
        "Enter replacment or press enter key to keep same: ")

    if new_number != "":
        for courier in couriers:
            if courier == selected_courier:
                selected_courier["phone number"] = new_number

    save_updated_couriers()
    load_file_couriers()
    return courier_menu()


def removal_of_courier():

    couriers.remove(selected_courier)
    save_updated_couriers()
    print("\nsuccessfully removed\n")
    load_file_couriers()
    return courier_menu()


def courier_menu():
    print("\nCourier Menu\n")
    print("To return to Main Menu enter 0")
    print("To view couriers enter 1")
    print("To add a new courier enter 2")
    print("To add a update courier enter 3")
    print("To remove a courier enter 4")
    global input3
    try:
        input3 = int(input("Where to: "))
        if input3 == 0:
            return return_to_main_menu()
        elif input3 == 1:
            return view_couriers_list()
        elif input3 == 2:
            return create_new_courier()
        elif input3 == 3:
            return get_courier()
        elif input3 == 4:
            return get_courier()
        else:
            print("\nInvalid input!\nReturning to courier menu")
            return product_menu()
    except ValueError:
        print("\nInvalid input!\nReturning to courier menu")
        return courier_menu()


# --------------------------------------File Handling----------------------------------------------------

import csv

def load_file_products():
    with open("products list.csv", mode = 'r') as file:
        reader = csv.DictReader(file, delimiter=',')
        print("\nProducts list:")
        global products
        products = []
        for i, row in enumerate(reader):
            i += 1
            print(i,row)
            products.append(row)


def load_file_couriers():
    with open("couriers list.csv", mode = 'r') as file:
        reader = csv.DictReader(file, delimiter=',')
        print("\nCouriers list:")
        global couriers
        couriers =[]
        for i, row in enumerate(reader):
            i += 1
            print(i, row)
            couriers.append(row)


def load_file_orders():
    with open("orders list.csv", mode = 'r') as file:
        reader = csv.DictReader(file, delimiter=',')
        print("\nOrders list:")
        global orders
        orders =[]
        for i, row in enumerate(reader):
            i += 1
            print(i, row)
            orders.append(row)


def add_new_product_file():
    with open("products list.csv", mode = 'a') as file:
        writer = csv.DictWriter(file, delimiter=',', fieldnames = ["name", "price"])
        writer.writerow(new_product)


def add_new_courier_file():
    with open("couriers list.csv", mode = 'a') as file:
        writer = csv.DictWriter(file, delimiter=',', fieldnames = ["name", "phone number"])
        writer.writerow(new_courier)


def add_new_order_file():
    with open("orders list.csv", mode='a') as file:
        writer = csv.DictWriter(file, delimiter=',', fieldnames=[
                                "name", "address", "phone number","courier", "status", "items"])
        writer.writerow(new_order)


def save_updated_products():
    with open("products list.csv", mode = 'w') as file:
        writer = csv.DictWriter(file, delimiter=',', fieldnames =["name", "price"])
        writer.writeheader()
        for product in products:
            writer.writerow(product)


def save_updated_couriers():
    with open("couriers list.csv", mode = 'w') as file:
        writer = csv.DictWriter(file, delimiter=',',fieldnames=["name", "phone number"])
        writer.writeheader()
        for courier in couriers:
            writer.writerow(courier)


def save_updated_orders():
    with open("orders list.csv", mode='w') as file:
        writer = csv.DictWriter(file, delimiter=',', fieldnames=[
                                "name", "address", "phone number", "courier", "status", "items"])
        writer.writeheader()
        new_orders_list = sorted(orders, key = lambda i: i["courier"])
        for order in new_orders_list:
            writer.writerow(order)


def checking_file_existance_products():
    import os.path

    if os.path.isfile("products list.csv"):
        return load_file_products()
    else:
        save_updated_products()
        load_file_products()


def checking_file_existance_couriers():
    import os.path

    if os.path.isfile("couriers list.csv"):
        return load_file_couriers()
    else:
        save_updated_couriers()
        load_file_couriers()


def checking_file_existance_orders():
    import os.path

    if os.path.isfile("orders list.csv"):
        return load_file_orders()
    else:
        save_updated_orders()
        load_file_orders()

# --------------------------------------Orders----------------------------------------------------


orders = [{"name": "Ron",
           "address": "123 weasly farm",
           "phone number": "12345678909",
           "courier": 2,
           "status": "on the way",
           "items": "1,3"
           },
          {"name": "Dan",
           "address": "789 king street",
           "phone number": "12345678909",
           "courier": 1,
           "status": "preparing",
           "items": "2,3,4"
           }
          ]


def order_menu():

    print("\nOrder Menu\n")
    print("To return to Main Menu enter         0")
    print("To view orders enter                 1")
    print("To add a new order enter             2")
    print("To add a update order status enter   3")
    print("To update an order enter             4")
    print("To remove a order enter              5")
    global input4

    input4 = int(input("Where to: "))
    try:
        if input4 == 0:
            print("\nReturning to main menu\n")
            return main_menu()
        elif input4 == 1:
            print("\nOrders:\n")
            return view_orders()
        elif input4 == 2:
            print("\nNew Order:\n")
            return add_new_order()
        elif input4 == 3:
            print("\nUpdate Order Status:\n")
            return get_order()
        elif input4 == 4:
            print("\nUpdate an Order:\n")
            return get_order()
        elif input4 == 5:
            print("\nRemove an order\n")
            return get_order()
        else:
            print("Invalid input\nTry again")
            return order_menu()
    except ValueError:
        print("\nInvalid Input\n")


def view_orders():
    load_file_orders()
    return order_menu()


def choose_a_courier():

    for i, courier in enumerate(couriers):
        i += 1
        print(i, courier)

    chosen = int(input("choose a courier from the list: "))
    
    chosen -= 1

    if chosen != (i - 1):
        print("error")
        return choose_a_courier()
    else:
        print("it works")
    print(chosen)

def add_new_order():

    try:

        name = str(input("Customer name: "))
        if name != "":
            name = name.title()
        else:
            print("\nDo not leave blank. Try again\n")
            return add_new_order()

        address = str(input("Customer address: "))
        if address != "":
            address = address.title()
        else:
            print("\nDo not leave blank. Try again\n")
            return add_new_order()

        phone_num = int(input("Customer phone number: "))

        # load_file_couriers()

        for i, courier in enumerate(couriers):
            i += 1
            print(i, courier)

        chosen_courier = int(input("\nPlease choose a courier from the list above: "))
        chosen_courier = str(chosen_courier)

        if chosen_courier != (i - 1):
            print("\nNot in the list. Try again\n")
            return add_new_order()

        order_status = "preparing"

        load_file_products()
        chosen_items = int(input("\nPlease select products from list above, use comma (,) to seperate items: "))

    except ValueError:
        print("value error")
        return add_new_order()
    
    

    global new_order

    new_order = {"name": name,
             "address": address,
             "phone number": phone_num,
             "courier": chosen_courier,
             "status": order_status,
             "items": chosen_items
             }
    orders.append(new_order)
    add_new_order_file()
    save_updated_orders()
    print("\nOrder has been added\n")
    load_file_orders()

    return order_menu()


def get_order():
    load_file_orders()

    try:

        selected = int(input("select order or 0 to cancel: "))
        if selected == 0:
            print("\nReturning to Order menu\n")
            return order_menu()

        selected -= 1

        global selected_order

        selected_order = orders[selected]
        print(selected_order)

    except ValueError:
        print("Invalid entry\nReturning to order menu")
        return order_menu()

    except IndexError:
        print("\nInvalid entry\nTry again")
        return order_menu()
    try:
        if input4 == 3:
            return update_status()
        elif input4 == 4:
            return update_order()
        elif input4 == 5:
            return remove_order()
    except ValueError:
        print("\nInvalid input\n")
        return order_menu()


def update_status():

    print("1: preparing")
    print("2: on the way")
    print("3: delivered")

    new_status = int(input("Select new status: "))


    if new_status == 1:
        new_status = "preparing"
    elif new_status == 2:
        new_status = "on the way"
    elif new_status == 3:
        new_status = "delivered"

    for order in orders:
        if order == selected_order:
            selected_order["status"] = new_status

    save_updated_orders()
    load_file_orders()
    return order_menu()


def update_order():

    print("\nUpdate name")
    update_message = input(
        "Enter replacment or press enter key to keep same: ")
    new_name = update_message

    if new_name != "":
        for order in orders:
            if order == selected_order:
                selected_order["name"] = new_name

    print("\nUpdate address ")
    new_address = input(
        "Enter replacment or press enter key to keep same: ")

    if new_address != "":
        for order in orders:
            if order == selected_order:
                selected_order["address"] = new_address

    print("\nUpdate phone number ")
    new_number = input(
        "Enter replacment or press enter key to keep same: ")

    if new_number != "":
        for order in orders:
            if order == selected_order:
                selected_order["phone number"] = new_number

    # load_file_couriers()
    print("\n")
    for i, courier in enumerate(couriers):
        i += 1
        print(i, courier)

    print("\nUpdate courier")
    new_courier_orders = input(
        "Enter replacment or press enter key to keep same: ")

    if new_courier_orders != "":

        if new_courier_orders != (i - 1):
            print("\nNot in the list. Try again\n")
            return update_order()

        for order in orders:
            if order == selected_order:
                selected_order["courier"] = new_courier_orders

    print("\nOrder status'\n")
    print("1: preparing")
    print("2: on the way")
    print("3: delivered")

    print("\nUpdate status")

    new_status = input(
        "Enter replacment or press enter key to keep same: ")


    if new_status != "":

        if new_status == 1:
            new_status = "preparing"
        elif new_status == 2:
            new_status = "on the way"
        elif new_status == 3:
            new_status = "delivered"

        for order in orders:
            if order == selected_order:
                selected_order["status"] = new_status


    load_file_products()
    print("\nUpdate items")
    new_items = input("Enter replacements with comma (,) seperator or press enter key to keep same: ")

    if new_items != "":
        for order in orders:
            if order == selected_order:
                selected_order["items"] = new_items


    save_updated_orders()
    load_file_orders()
    return order_menu()


def remove_order():

    try:
        orders.remove(selected_order)
        save_updated_orders()
        print("\nsuccessfully removed\n")
        load_file_orders()
        return order_menu()
    except IndexError:
        print("Index error")


# --------------------------------------Executing Code----------------------------------------------------


# checking_file_existance_products()
# checking_file_existance_couriers()
# checking_file_existance_orders()
# main_menu()
choose_a_courier()
