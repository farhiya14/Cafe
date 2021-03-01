import app

orders = [{"name": "Tom",
           "address": "123 queen street",
           "phone number": "12345678909",
           "courier": 2,
           "status": "on the way"
           },
          {"name": "Dan",
           "address": "789 king street",
           "phone number": "12345678909",
           "courier": 1,
           "status": "preparing"
           }
          ]


def order_menu():

    print("\nOrder Menu\n")
    print("To return to Main Menu enter 0")
    print("To view orders enter 1")
    print("To add a new order enter 2")
    print("To add a update order status enter 3")
    print("To add a update order enter 4")
    print("To remove a order enter 5 ")
    global input4

    input4 = int(input("Where to: "))
    try:
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
        print("\nInavlid entry!\nTry again\n")
        return order_menu()


def view_orders():
    print("Orders\n")
    for i, order in enumerate(orders):
        i += 1
        print(i, ":", order)
    return order_menu()


def add_new_order():
    name = str(input("Customer name: "))
    name = name.title()

    address = str(input("Customer address: "))
    address = address.title()

    phone_num = int(input("Customer phone number: "))

    # TODO: figure out how to get courier name insted of there number
    for i, courier in enumerate(app.couriers):
        i += 1
        print(i, courier)
    chosen_courier = int(
        input("Please choose a courier from the list above: "))

    order_status = "preparing"

    order = {"name": name,
             "address": address,
             "phone number": phone_num,
             "courier": chosen_courier,
             "status": order_status
             }
    orders.append(order)

    print("\nOrder has been added\n")
    print("\n", orders, "\n")
    return order_menu()


def get_order():

    for i, order in enumerate(orders):
        i += 1
        print(i, order)

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
        print("\nInvalid input\nEnter a number\n")
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

    return view_orders()


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

    print("\nCouriers:\n")
    for i, courier in enumerate(app.couriers):
        i += 1
        print(i, courier)

    print("\nUpdate courier")
    new_courier_orders = input(
        "Enter replacment or press enter key to keep same: ")

    if new_courier_orders != "":
        for order in orders:
            if order == selected_order:
                selected_order["courier"] = new_courier_orders

    print("\nOrder status'\n")
    print("1: preparing")
    print("2: on the way")
    print("3: delivered")

    print("\nUpdate status")

    update_status = int(input(
        "Enter replacment or press enter key to keep same: "))

    if update_status != "":
    
        if update_status == 1:
            update_status = "preparing"
        elif update_status == 2:
            update_status = "on the way"
        elif update_status == 3:
            update_status = "delivered"

        for order in orders:
            if order == selected_order:
                selected_order["status"] = update_status

    return view_orders()


def remove_order():

    try:
        orders.remove(selected_order)
        print("\nsuccessfully removed\n")
        return view_orders()
    except IndexError:
        print("Index error")


order_menu()

# Everything works TODO: Handle errors use try and except, then do unit tests
