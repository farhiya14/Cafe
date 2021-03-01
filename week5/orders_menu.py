import app


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

    try:
        input4 = int(input("Where to: "))

        if input4 == 0:
            print("\nReturning to main menu\n")
            return app.main_menu()
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


    choose_a_courier()

    order_status = "preparing"

    product_selection()

    if selected_items == 0:
        return order_menu ()

    global new_order

    new_order = {"name": name,
                 "address": address,
                 "phone number": phone_num,
                 "courier": chosen_courier,
                 "status": order_status,
                 "items": selected_items
                 }
    orders.append(new_order)
    add_new_order_file()
    save_updated_orders()
    print("\nOrder has been added\n")
    load_file_orders()

    return order_menu()


def choose_a_courier():

    for i, courier in enumerate(app.couriers):
        i += 1
        print(i, courier)

    global chosen_courier

    try:
        chosen_courier = int(
            input("\nPlease choose a courier from the list above: "))

        if chosen_courier == 0:
            print("choose from the list")
            return choose_a_courier()

        chosen_courier -= 1

        print(app.couriers[chosen_courier])

        #un comment if you want to sort orders my courier
        # chosen_courier = str(chosen_courier)

        chosen_courier += 1

    except ValueError:
        print("invalid input")
        return choose_a_courier()

    except IndexError:
        print("invalid input")
        return choose_a_courier()


def product_selection():
    
    for i, product in enumerate(app.products):
        i += 1
        print(i,product)

    global selected_items

    selected_items = input("\nPlease select products from list above, use comma(,) to seperate items or 0 to cancel: ")
    selected_items = selected_items.rstrip()  

    if selected_items == '0':
        print("cancelling order")
        return order_menu()
    items = []
    items.append(selected_items)
    print(items)

    new_list = []
    new_list_2 = []

    for item in items:
        new_list = (item.split(","))
    print(new_list)

    def is_integer(item):
        try:
            float(item)
        except ValueError:
            return False
        else:
            return float(item).is_integer()

    try:
        for item in new_list:
            if is_integer(item) == True:
                item = int(item)
                item -= 1
                new_list_2.append(app.products[item])
            else:
                print("'{}' is not a valid input and has not been added to list".format(item))
                continue

        print(new_list_2)

        return new_list

    except IndexError:
        print("\nIndex Error. Select a valid inputs\n")
        print("'{}' is not valid input".format((item + 1)))
        return product_selection()
    except ValueError:
        print("'{}' is not valid input2".format((item)))
        return product_selection()


def get_order():
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

    except ValueError:
        print("Invalid entry\n")
        return get_order()

    except IndexError:
        print("\nInvalid entry\nTry again\n")
        return get_order()
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


def update_order():

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


    def choose_a_courier_2():

        for i, courier in enumerate(app.couriers):
            i += 1
            print(i, courier)
        
        print("\nUpdate courier")
        new_courier = input("Enter replacment or press enter key to keep same: ")

        try:
            new_courier = int(new_courier)
            new_courier -= 1

            #un comment if you want to sort orders my courier
            # chosen_courier = str(chosen_courier)

            for order in orders:
                if order == selected_order:
                    selected_order["courier"] = (app.couriers[new_courier]["id"])
        except ValueError:
            if new_courier == "":
                pass
            else:
                print("Invalid entry\nTry again1")
                return choose_a_courier_2()
        except IndexError:
            print("invalid input")
            return choose_a_courier_2()

    choose_a_courier_2()


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

    update_new_status()


    #edit to se
    app.load_file_products()
    print("\nUpdate items")
    new_items = input(
        "Enter replacements with comma (,) seperator or press enter key to keep same: ")

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
        return remove_order()


import csv

def add_new_order_file():
    with open("orders list.csv", mode='a') as file:
        writer = csv.DictWriter(file, delimiter=',', fieldnames=[
                                "name", "address", "phone number", "courier", "status", "items"])
        writer.writerow(new_order)


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


def save_updated_orders():
    with open("orders list.csv", mode='w') as file:
        writer = csv.DictWriter(file, delimiter=',', fieldnames=[
                                "name", "address", "phone number", "courier", "status", "items"])
        writer.writeheader()
        # new_orders_list = sorted(orders, key=lambda i: i["status"])
        for order in orders: #new_orders_list:
            writer.writerow(order)


def checking_file_existance_orders():
    import os.path

    if os.path.isfile("orders list.csv"):
        return load_file_orders()
    else:
        save_updated_orders()
        load_file_orders()

# checking_file_existance_orders()
# order_menu()


# # if __name__ == '__main__':
# #     update_order()
