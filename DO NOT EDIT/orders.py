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
    # try:
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
    # except ValueError:
    #     print("\nInavlid entry! Try again\n")
    #     return order_menu()


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

    phone_num = str(input("Customer phone number: "))

    ##FIX ME: get user selection (actually not neccessary yet) ~ this method is needed again
    for i, courier in enumerate(app.couriers):
        i += 1
        print(i, courier)
    chosen_courier = int(input("Please choose a courier from the list above: "))
    # chosen_courier = (chosen_courier - 1)
    # chosen_courier = courier.index(chosen_courier)

    order_status = "preparing"
 


    order = {"name": name,
             "address": address,
             "phone number": phone_num,
             "courier": chosen_courier,
             "status": order_status
             }
    orders.append(order)

    print("Order has been added\n")
    print(orders)
    return order_menu()


def get_order():

    for i, order in enumerate(orders):
        i += 1
        print(i, order)

    selected = int(input("select order or 0 to canel: "))
    if selected == 0:
        print("\nReturning to Order menu\n")
        return order_menu()
    
    selected -= 1

    global selected_order

    selected_order = orders[selected]
    # print(selected_order)
    
    if input4 == 3:
        return update_status()
    elif input4 == 4:
        return update_order()
    elif input4 == 5:
        return remove_order()


def update_status():

    print("1: preparing")
    print("2: on the way")
    print("3: delivered")

    new_status = int(input("Select new status: "))

    if new_status == 1:
        new_status = "preparing"
    elif new_status == 2:
        new_status= "on the way"
    elif new_status == 3:
        new_status = "delivered"


    for order in orders:
        if order == selected_order:
            selected_order["status"] = new_status
            # print(selected_order)
            view_orders()
        else:
            print("ERROR")


def update_order():
    print("Works")
    return None


def remove_order():
    
    orders.remove(selected_order)
    print("\nsuccessfully removed\n")
    
    return view_orders()


order_menu()
