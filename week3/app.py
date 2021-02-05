products = ["Coke", "Coffee"]

couriers = ["Jack Johnson", "Man Bun"]


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
            return exit
        elif input1 == 1:
            return product_menu()
        elif input1 == 2:
            return courier_menu()
        elif input1 == 3:
            import orders
            return orders.order_menu()
        else:
            print("\nInvalid Input!")
            return main_menu()
    except ValueError:
        print("\nInvalid Input!")
        return main_menu()


def return_to_main_menu():
    print("Return to Main Menu")
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
    new_product = input("Enter name of new product: ")
    new_product = new_product.title()
    confirmation = int(
        input("Is this correct '{}'? Enter 0 for yes and 1 for no: ".format(new_product)))
    try:
        if confirmation == 0:
            if new_product in products:
                print("{} is already in the list.\nReturning to product menu".format(
                    new_product))
                return product_menu()
            else:
                print("{} has been added to product list\n".format(new_product))
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


def update_product():
    try:
        updating_product = input("Enter name of product you wish to update: ")
        updating_product = updating_product.title()
        confirmation_update = int(input(
            "Is this correct '{}'? Enter 0 for yes and 1 for no: ".format(updating_product)))
        if confirmation_update == 1:
            print("\nReturning to product menu\n")
            return product_menu()
        elif confirmation_update == 0:
            if updating_product in products:
                updated_product = input("Replace product with: ")
                updated_product = updated_product.title()
                update_confirmation = int(input(
                    "Is this correct '{}'? Enter 0 for yes and 1 for no: ".format(updated_product)))
                if update_confirmation == 0:
                    if update_product in products:
                        print("Product already in list\nReturning to product menu\n")
                        return product_menu()
                    else:
                        index = products.index(updating_product)
                        products.remove(updating_product)
                        products.insert(index, updated_product)
                        save_updated_products()
                        print("Here is an updated product list:\n")
                        load_file_products()
                        print("\nReturnig to product menu\n")
                        return product_menu()
                elif update_confirmation == 1:
                    print("Returning to product menu")
                    return product_menu()
                else:
                    print("Invalid input!\nReturning to product menu")
                    return product_menu()
            else:
                print("\nThat Product does not exist!\nReturning to product menu")
                return product_menu()
        else:
            print("\nInvalid input!\nReturning to product menu")
            return product_menu()
    except ValueError:
        print("\nInvalid Entry!\nReturning to product menu\n")
        return product_menu()


def remove_product():
    try:
        removing_product = input("Enter name of product you wish to remove: ")
        removing_product = removing_product.title()
        removal_confirmation = int(input(
            "Is this correct '{}'? Enter 0 for yes and 1 for no: ".format(removing_product)))
        if removal_confirmation == 0:
            if removing_product in products:
                products.remove(removing_product)
                save_updated_products()
                print("Updated product list:\n")
                load_file_products()
                return product_menu()
            else:
                print(
                    "That item is not in the products list.\nReturning to product menu.")
                return product_menu()
        elif removal_confirmation == 1:
            print("Returning to product menu")
            return product_menu()
        else:
            print("\nInvalid input!\nReturning to product menu")
            return product_menu()
    except ValueError:
        print("Invalid input!\nReturning to product menu")
        return product_menu()


def product_menu():
    print("\nProduct Menu\n")
    print("To return to Main Menu enter 0")
    print("To view products enter 1")
    print("To add a new product enter 2")
    print("To add a update product enter 3")
    print("To remove a product enter 4")
    input2 = int(input("Where to: "))

    try:
        if input2 == 0:
            return return_to_main_menu()
        elif input2 == 1:
            return view_products_list()
        elif input2 == 2:
            return create_new_product()
        elif input2 == 3:
            return update_product()
        elif input2 == 4:
            return remove_product()
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
    new_courier = input("Enter name of new courier: ")
    new_courier = new_courier.title()
    confirmation = int(
        input("Is this correct '{}'? Enter 0 for yes and 1 for no: ".format(new_courier)))
    try:
        if confirmation == 0:
            if new_courier in couriers:
                print("{} is already in the list.\n\nReturning to product menu".format(
                    new_courier))
                return courier_menu()
            else:
                print("{} has been added to couriers list\n".format(new_courier))
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


def update_courier():
    try:
        updating_courier = input("Enter name of courier you wish to update: ")
        updating_courier = updating_courier.title()
        confirmation_update = int(input(
            "Is this correct '{}'? Enter 0 for yes and 1 for no: ".format(updating_courier)))
        if confirmation_update == 1:
            print("\nReturning to courier menu\n")
            return courier_menu()
        elif confirmation_update == 0:

            if updating_courier in couriers:
                updated_courier = input("Replace couriers with: ")
                updated_courier = updated_courier.title()
                update_confirmation = int(input(
                    "Is this correct '{}'? Enter 0 for yes and 1 for no: ".format(updated_courier)))
                if update_confirmation == 0:

                    if update_courier in couriers:
                        print("Courier already exists\nReturning ot courier menu")
                        return courier_menu()
                    else:
                        index = couriers.index(updating_courier)
                        couriers.remove(updating_courier)
                        couriers.insert(index, updated_courier)
                        save_updated_couriers()
                        print("\nHere is an updated couriers list:\n ")
                        load_file_couriers()
                        print("\nReturnig to couriers menu\n")
                        return courier_menu()

                elif update_confirmation == 1:
                    print("Returning to couriers menu")
                    return courier_menu()
                else:
                    print("Invalid input!\nReturning to courier menu")
                    return courier_menu()
            else:
                print("\nThat courier does not exist!\nReturning to couriers menu")
                return courier_menu()
        else:
            print("\nInvalid input!\nReturning to courier menu")
            return product_menu()

    except ValueError:
        print("\nInvalid input!\nReturning to courier menu")
        return courier_menu()


def remove_courier():
    try:
        removing_courier = input("Enter name of courier you wish to remove: ")
        removing_courier = removing_courier.title()
        removal_confirmation = int(input(
            "Is this correct '{}'? Enter 0 for yes and 1 for no: ".format(removing_courier)))
        if removal_confirmation == 0:
            if removing_courier in couriers:
                couriers.remove(removing_courier)
                save_updated_couriers()
                print("\nUpdated couriers list:\n")
                load_file_couriers()
                return courier_menu()
            else:
                print(
                    "That item is not in the couriers list.\nReturning to courier menu.")
                return courier_menu()
        elif removal_confirmation == 1:
            print("Returning to courier menu")
            return courier_menu()
        else:
            print("\nInvalid input!\nReturning to courier menu")
            return product_menu()
    except ValueError:
        print("\nInvalid input!\nReturning to courier menu")
        return courier_menu()


def courier_menu():
    print("\nCourier Menu\n")
    print("To return to Main Menu enter 0")
    print("To view couriers enter 1")
    print("To add a new courier enter 2")
    print("To add a update courier enter 3")
    print("To remove a courier enter 4")
    try:
        input3 = int(input("Where to: "))
        if input3 == 0:
            return return_to_main_menu()
        elif input3 == 1:
            return view_couriers_list()
        elif input3 == 2:
            return create_new_courier()
        elif input3 == 3:
            return update_courier()
        elif input3 == 4:
            return remove_courier()
        else:
            print("\nInvalid input!\nReturning to courier menu")
            return product_menu()
    except ValueError:
        print("\nInvalid input!\nReturning to courier menu")
        return courier_menu()


# --------------------------------------File Handling----------------------------------------------------


def load_file_products():
    print("\nProducts:")
    with open("products list.txt", "r")as my_file:
        contents = print(str(my_file.read().rstrip()))
        return contents


def load_file_couriers():
    print("\nCouriers:")
    with open("couriers list.txt", "r") as my_file:
        contents = print(str(my_file.read().rstrip()))
        return contents


def add_new_product_file():
    my_file = open("products list.txt", "a")
    my_file.write(new_product + "\n")
    my_file.close()


def add_new_courier_file():
    my_file = open("couriers list.txt", "a")
    my_file.write(new_courier + "\n")
    my_file.close()


def save_updated_products():
    my_file = open("products list.txt", "w+")
    for product in products:
        my_file.write(product + "\n")
    my_file.close()


def save_updated_couriers():
    my_file = open("couriers list.txt", "w+")
    for courier in couriers:
        my_file.write(courier + "\n")
    my_file.close()


def checking_file_existance_products():
    import os.path

    if os.path.isfile("products list.txt"):
        return load_file_products()
    else:
        save_updated_products()
        load_file_products()


def checking_file_existance_couriers():
    import os.path

    if os.path.isfile("couriers list.txt"):
        return load_file_couriers()
    else:
        save_updated_couriers()
        load_file_couriers()


# checking_file_existance_products()
# checking_file_existance_couriers()
# main_menu()
