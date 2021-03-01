import os
products = [{"id": 1,
            "name": "Coke",
            "price": 0.8,
            },
            {"id": 2,
            "name": "Water",
            "price": 0.65 }]#// float, }]

couriers = [{"id": 1,
            "name": "Jack",
            "phone number": "7418529966375"},
            {"id": 2,
            "name": "Tom",
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
    
    os.system('clear')


def return_to_main_menu():
    print("\nReturn to Main Menu\n")
    os.system('clear')
    return main_menu()






















def check_id():
    id_prod = 1

    for order in orders:

        if id_prod == order["id"]:
            print(order["id"])
            print(id_prod," so")
            id_prod += 1
            
        else:
            print("nope")
            print(id_prod)
            
        return id_prod





# --------------------------------------Product Menu----------------------------------------------------
# os.system('clear')

def view_products_list():
    print("Products:\n")
    load_file_products(products)
    return product_menu()


def create_new_product():
    print("Products:\n")
    load_file_products(products)
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
                # product_id = check_id()
                
                new_product = { "id": check_id(),
                                "name": new_product_name,
                                "price": new_product_price}

                add_new_product_file()
                load_file_products(products)
                print("\nReturning to product menu")
                return product_menu()
        elif confirmation == 1:
            print("Returning to product menu")
            return product_menu()
        else:
            print("\nInvalid input!\nReturning to product menu1")
            return product_menu()
    except ValueError:
        print("Invalid input!\nReturning to product menu2")
        return product_menu()


def get_product():
    load_file_products(products)

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
        print("Invalid entry! Try again\n")
        return get_product()

    except IndexError:
        print("\nInvalid entry! Try again\n")
        return get_product()
    try:
        if input2 == 3:
            return update_products()
        elif input2 == 4:
            return removal_of_product()
    except ValueError:
        print("\nInvalid input\n")
        return get_product()


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
    
    save_updated_products(products)
    load_file_products(products)
    return product_menu()


def removal_of_product():

    try:
        products.remove(selected_product)
        save_updated_products(products)
        print("\nsuccessfully removed\n")
        load_file_products(products)
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
                courier_id = (couriers.index(new_courier) +1)

                new_courier = { "id": courier_id,
                                "name": new_courier_name,
                                "phone number": new_courier_number}

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
    
    for i, courier in enumerate(couriers):
        i += 1
        print(i, courier)

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

def load_file_products(products):
    with open("products list.csv", mode = 'r') as file:
        reader = csv.DictReader(file, delimiter=',')
        print("\nProducts list:")
        # global products
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
        writer = csv.DictWriter(file, delimiter=',', fieldnames=[
                                "id", "name", "price"])
        writer.writerow(new_product)


def add_new_courier_file():
    with open("couriers list.csv", mode = 'a') as file:
        writer = csv.DictWriter(file, delimiter=',', fieldnames = ["id","name", "phone number"])
        writer.writerow(new_courier)


def add_new_order_file(new_order):
    with open("orders list.csv", mode='a') as file:
        writer = csv.DictWriter(file, delimiter=',', fieldnames=[
                                "id", "name", "address", "phone number", "courier", "status", "items"])
        writer.writerow(new_order)


def save_updated_products(products):
    with open("products list.csv", mode = 'w') as file:
        writer = csv.DictWriter(file, delimiter=',', fieldnames=[
                                "id", "name", "price"])
        writer.writeheader()
        for product in products:
            # if product["id"] != products.index(product) + 1:
            #     product_id = products.index(product) + 1
            #     product["id"] = product_id
            writer.writerow(product)


def save_updated_couriers():
    with open("couriers list.csv", mode = 'w') as file:
        writer = csv.DictWriter(file, delimiter=',',fieldnames=["id","name", "phone number"])
        writer.writeheader()
        for courier in couriers:
            # if courier["id"] != couriers.index(courier) + 1:
            #     courier_id = couriers.index(courier) + 1
            #     courier ["id"] = courier_id
            writer.writerow(courier)


def save_updated_orders():
    with open("orders list.csv", mode='w') as file:
        writer = csv.DictWriter(file, delimiter=',', fieldnames=[
                                "id", "name", "address", "phone number", "courier", "status", "items"])
        writer.writeheader()
        new_orders_list = sorted(orders, key = lambda i: i["status"])
        for order in new_orders_list:
            writer.writerow(order)


def checking_file_existance_products():
    import os.path

    if os.path.isfile("products list.csv"):
        return load_file_products(products)
    else:
        save_updated_products(products)
        load_file_products(products)


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


orders = [{ "id": 1,
            "name": "Ron",
            "address": "123 weasly farm",
            "phone number": "12345678909",
            "courier": 2,
            "status": "on the way",
            "items": "1,2"
            },
            {"id": 2,
            "name": "Dan",
            "address": "789 king street",
            "phone number": "12345678909",
            "courier": 1,
            "status": "preparing",
            "items": "2,2,1"
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
    # global input4

    try:
        input4 = int(input("Where to: "))

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
            return get_order(input4)
        elif input4 == 4:
            print("\nUpdate an Order:\n")
            return get_order(input4)
        elif input4 == 5:
            print("\nRemove an order\n")
            return get_order(input4)
        else:
            print("Invalid input\nTry again")
            return order_menu()
    except ValueError:
        print("\nInvalid Input_menu\n")
        return order_menu()


def view_orders():
    load_file_orders()
    return order_menu()


def add_new_order():

    name = str(input("Customer name: "))
    name = name.title()

    while name == "":
        print("Do not leave blank\n")
        name = str(input("Customer name: "))
        name = name.title()

    address = str(input("Customer address: "))
    address = address.title()

    while address == "":
        print("Do not leave blank\n")
        address = str(input("Customer address: "))
        address = address.title()

    phone_num = input("Customer phone number: ")

    while phone_num == "" or len(phone_num) != 11 or phone_num.isdigit() == False:
        print("Enter a valid phone number\n")
        phone_num = input("Customer phone number: ")


    order_status = "preparing"




    new_order = {"id": id,
                "name": name,
                "address": address,
                "phone number": phone_num,
                "courier":  add_courier_new_order(),
                "status": order_status,
                "items": product_selection()
                }

    orders.append(new_order)
    add_new_order_file(new_order)
    save_updated_orders()
    print("\nOrder has been added\n")
    load_file_orders()

    return order_menu()


def add_courier_new_order():
    load_file_couriers()
    
    picked_courier = input("select a courier from the list: ")

    try:
            picked_courier = int(picked_courier)
            index = couriers.index(courier_selection(picked_courier)) + 1
            print(courier_selection(picked_courier))
            return index
    
    except ValueError:
        print("\nPlease select a number\n")
        return add_courier_new_order()


def is_integer(item):
    try:
        float(item)
    except ValueError:
        return False
    else:
        return float(item).is_integer()


def product_selection():

    load_file_products(products)

    selected_items = input("\nPlease select products from list above, use comma(,) to seperate items or 0 to cancel: ")
    selected_items = selected_items.strip()

    if selected_items == '0':
        print("cancelling order")
        return order_menu()

    selected_products_dicts = []
    show = []

    ordered_products = (selected_items.split(","))
    print(ordered_products)


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

        # print(show)
        print(selected_products_dicts)

    except IndexError:
        print("\nIndex Error. Select a valid inputs\n")
        print("'{}' is not valid input".format((item)))
        return product_selection()
    
    except ValueError:
        print("'{}' is not a valid input and has not been added to list".format(item))
        return product_selection()
    
    finally:
        new_3 = ""

        for item in show:
            new_3 = new_3 + str(item) + ","
        
        print(new_3[:-1])
        return new_3[:-1]



def get_order(input4):
    load_file_orders()
    #get rid of try and swap with while
    try:
        selected = int(input("select order or 0 to cancel: "))

        while selected == "":
            selected = int(input("select order or 0 to cancel: "))

        if selected == 0:
            print("\nReturning to Order menu\n")
            return order_menu()

        selected -= 1

        global selected_order

        selected_order = orders[selected]
        print(selected_order)

        return selected_order

    except ValueError:
        print("Invalid entry\n")
        return get_order(input4)

    except IndexError:
        print("\nInvalid entry\nTry again\n")
        return get_order(input4)
    try:
        if input4 == 3:
            return update_status()
        elif input4 == 4:
            return update_order()
        elif input4 == 5:
            return remove_order()
    except ValueError:
        print("\nInvalid input_get_order\n")
        return order_menu()


def update_status():

    print("1: preparing")
    print("2: on the way")
    print("3: delivered")
    try:
        new_status = int(input("Select new status: "))

        if new_status == 1:
            new_status = "preparing"
        elif new_status == 2:
            new_status = "on the way"
        elif new_status == 3:
            new_status = "delivered"
        else:
            print("please enter from available list")
            return update_status()

        for order in orders:
            if order == selected_order:
                selected_order["status"] = new_status
    except IndexError:
        print("not right")
        return update_status()
    except ValueError:
        print("not right2")
        return update_status()

    save_updated_orders()
    load_file_orders()
    return order_menu()


def get_new_values():
    
    print("\nUpdate name")
    new_name = input(
        "Enter replacment or press enter key to keep same: ")

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


def update_new_status():

    print("\nUpdate status")

    print("1: preparing")
    print("2: on the way")
    print("3: delivered")

    new_status = input(
        "Enter replacment or press enter key to keep same: ")

    try:
        new_status = int(new_status)
        if new_status != "":
            if new_status == 1:
                new_status = "preparing"
            elif new_status == 2:
                new_status = "on the way"
            elif new_status == 3:
                new_status = "delivered"
            else:
                print("please enter from available list")
                return update_new_status()

            for order in orders:
                if order == selected_order:
                    selected_order["status"] = new_status
        else:
            pass
    except IndexError:
        print("not right")
        return update_new_status()
    except ValueError:
        if new_status == "":
            pass
        else:
            print("not right2")
            return update_new_status()


def courier_selection(picked):

    try:
        picked -= 1
        # print(couriers[picked])
        return couriers[picked]

    except IndexError:
        print("idx error")
        return update_courier()


def update_courier():
    load_file_couriers()

    picked_courier = input(
        "Enter replacment or press enter key to keep same: ")

    try:
        if picked_courier != "":
            picked_courier = int(picked_courier)
            index = couriers.index(courier_selection(picked_courier)) + 1
            print(courier_selection(picked_courier))

            for order in orders:
                if order == selected_order:
                    selected_order["courier"] = index

    except IndexError:
        print("wrong index")
        return update_courier()
    
    except ValueError:
        if picked_courier == "":
            pass


def update_product_selection():

    try:
        product_selection()

        for order in orders:
            if order == selected_order:
                selected_order["items"] = product_selection()

    except ValueError:
        if product_selection() == "" or []:
            pass
        else:
            return update_product_selection()


def update_order():

    get_new_values()

    update_courier()

    update_new_status()

    update_product_selection()

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
        return remove_order()


# def add_new_order_file():
#     with open("orders list.csv", mode='a') as file:
#         writer = csv.DictWriter(file, delimiter=',', fieldnames=[
#                                 "name", "address", "phone number", "courier", "status", "items"])
#         writer.writerow(new_order)


# def load_file_orders():
#     with open("orders list.csv", mode='r') as file:
#         reader = csv.DictReader(file, delimiter=',')
#         print("\nOrders list:")
#         global orders
#         orders = []
#         for i, row in enumerate(reader):
#             i += 1
#             print(i, row)
#             orders.append(row)


# def save_updated_orders():
#     with open("orders list.csv", mode='w') as file:
#         writer = csv.DictWriter(file, delimiter=',', fieldnames=[
#                                 "name", "address", "phone number", "courier", "status", "items"])
#         writer.writeheader()
#         # new_orders_list = sorted(orders, key=lambda i: i["status"])
#         for order in orders:  # new_orders_list:
#             writer.writerow(order)


# def checking_file_existance_orders():
#     import os.path

#     if os.path.isfile("orders list.csv"):
#         return load_file_orders()
#     else:
#         save_updated_orders()
#         load_file_orders()


# --------------------------------------Executing Code----------------------------------------------------


checking_file_existance_products()
checking_file_existance_couriers()
checking_file_existance_orders()
main_menu()
# order_menu()
# create_new_product()


# if __name__ == '__main__':
#     update_order()
