

orders = [{"name": "hi",
           "age": 17},
          {"name": "low",
           "age": 54}]


def get_order():
    for i, order in enumerate(orders):
        i += 1
        print(i, order)

    selected = int(input("select order: "))
    selected -= 1

    global selected_order

    selected_order = orders[selected]
    print(selected_order)
    return update_age()


def update_age():

    new_age = int(input("new age: "))

    for order in orders:
        if order == selected_order:
            selected_order["age"] = new_age
            print(selected_order)
            print(orders)
        break

get_order()
