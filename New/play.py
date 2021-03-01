# products = []

import csv
import os



def create_new_product():
    os.system('clear')

    print("\nAdd New Product\n")
    products = filing()


    add_product_to_list(product_id(), new_name(), new_price())

    os.system('clear')

    return products 


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
        # return new_product_name
    elif confirm == 1:
        return new_name()
    else:
        return new_name()

    return new_product_name


def new_price():
    try:

        new_price = float(
            input("Enter product price "))

    except ValueError:
        print("please enter a valid input")
        return new_price()

    finally:
        return new_price


def product_id():
    try:

        last_product_in_list = products[-1]

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

    products.append(new_product)

    filing()

    return new_product



def filing():
    products = []
    with open("play list.csv", mode='r+') as file:
        writer = csv.DictWriter(file, delimiter=',', fieldnames=["id", "name", "price"])
        writer.writeheader()
        for product in products:
            writer.writerow(product)
        print(products)
        return products


products = filing()

print("\n")
create_new_product()



filing()