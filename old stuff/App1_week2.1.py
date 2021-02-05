products = ["Coke", "Coke Zero", "Fanta Orange", "Water", "Coffee"]

couriers = ["Jack Johnson"]


def main_menu():
    try:
        print("\nMain Menu")
        print("\nTo exit app enter 0")
        print("To go to Product Menu enter 1")
        print("To go to Courier Menu enter 2")
        input1 = int(input("Where to: "))
        if input1 == 0:
            print("Exiting App")
            return exit
        elif input1 == 1:
            return product_menu()
        elif input1 == 2:
            return courier_menu()
        else:
            print("\nInvalid Input!")
            return main_menu()
    except ValueError:
        print("\nInvalid Input!")
        return main_menu()


def return_to_main_menu():
    print("Return to Main Menu")
    return main_menu()


def view_products_list():
    print("Products:")
    return read_products_txt() and product_menu()


def create_new_product():
    try:
        read_products_txt()
        print("Create new product")
        new_product = input("Enter name of new product: ")
        new_product = new_product.title()
        confirmation = int(
            input("Is this correct '{}'? Enter 0 for yes and 1 for no: ".format(new_product)))
        if confirmation == 0:
            if new_product in products:
                print("{} is already in the list.\nReturning to product menu".format(
                    new_product))
                return product_menu()
            else:
                print("{} has been added to product list".format(new_product))
                products.append(new_product)
                print(products, "\n\nReturning to product menu")
                update_products_txt()
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
        read_products_txt()
        updating_product = input("Enter name of product you wish to update: ")
        updating_product = updating_product.title()
        confirmation_update = int(input(
            "Is this correct '{}'? Enter 0 for yes and 1 for no: ".format(updating_product)))
        if confirmation_update == 1:
            print("\nReturning to product menu")
            return product_menu()
        elif confirmation_update == 0:
            if updating_product in products:
                updated_product = input("Replace product with: ")
                updated_product = updated_product.title()
                update_confirmation = int(input(
                    "Is this correct '{}'? Enter 0 for yes and 1 for no: ".format(updated_product)))
                if update_confirmation == 0:
                    index = products.index(updating_product)
                    products.remove(updating_product)
                    products.insert(index, updated_product)
                    print("Here is an updated product list: ",
                        products, "\nReturnig to product menu ")
                    update_products_txt()
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
        read_products_txt()
        removing_product = input("Enter name of product you wish to remove: ")
        removing_product = removing_product.title()
        removal_confirmation = int(input(
            "Is this correct '{}'? Enter 0 for yes and 1 for no: ".format(removing_product)))
        if removal_confirmation == 0:
            if removing_product in products:
                products.remove(removing_product)
                print("Updated product list: ", products)
                update_products_txt()
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
    try:
        input2 = int(input("Where to: "))

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


def view_couriers_list():
    print("Couriers:")
    read_couriers_txt()
    return courier_menu()

def create_new_courier():
    print("\nCourier list:\n")
    read_couriers_txt()
    print("Create new courier")
    new_courier = input("Enter name of new courier: ")
    new_courier = new_courier.title()
    confirmation = int(
        input("Is this correct '{}'? Enter 0 for yes and 1 for no: ".format(new_courier)))
    if confirmation == 0:
        if new_courier in couriers:
            print("{} is already in the list.\n\nReturning to product menu".format(
                new_courier))
            return courier_menu()
        else:
            print("{} has been added to couriers list".format(new_courier))
            couriers.append(new_courier)
            update_couriers_txt()
            # print(couriers)
            # read_couriers_txt()
            return courier_menu()
    elif confirmation == 1:
        print("Returning to courier menu")
        return courier_menu()

# def create_new_courier():
# # try:
#     print("\nCourier list:\n")
#     read_couriers_txt()
#     print("Create new courier")
#     new_courier = input("Enter name of new courier: ")
#     new_courier = new_courier.title()
#     confirmation = int(
#         input("Is this correct '{}'? Enter 0 for yes and 1 for no: ".format(new_courier)))
#     if confirmation == 0:
#         if new_courier in couriers:
#             print("{} is already in the list.\n\nReturning to product menu".format(
#                 new_courier))
#             return courier_menu()
#         else:
#             print("{} has been added to couriers list".format(new_courier))
#             couriers.append(new_courier)
#             update_couriers_txt()
#             # print(couriers)
#             # read_couriers_txt()
#             return courier_menu()
#     elif confirmation == 1:
#         print("Returning to courier menu")
#         return courier_menu()
#     # elif confirmation != 1 and confirmation != 0:
#     #     print("\nInvalid input!\nReturning to courier menu")
#     #     return courier_menu()
# # except ValueError:
# #     print("\nInvalid input!\nReturning to courier menu")
# #     return  courier_menu()


def update_courier():
    try:
        read_couriers_txt()
        updating_courier = input("Enter name of courier you wish to update: ")
        updating_courier = updating_courier.title()
        confirmation_update = int(input(
            "Is this correct '{}'? Enter 0 for yes and 1 for no: ".format(updating_courier)))
        if confirmation_update == 1:
            print("Returning to courier menu")
            return courier_menu()
        elif confirmation_update == 0:
            if updating_courier in couriers:
                updated_courier = input("Replace couriers with: ")
                updated_courier = updated_courier.title()
                update_confirmation = int(input(
                    "Is this correct '{}'? Enter 0 for yes and 1 for no: ".format(updated_courier)))
                if update_confirmation == 0:
                    index = couriers.index(updating_courier)
                    couriers.remove(updating_courier)
                    couriers.insert(index, updated_courier)
                    print("Here is an updated couriers list: ",
                        couriers, "\nReturnig to couriers menu ")
                    update_couriers_txt()
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
        read_couriers_txt()
        removing_courier = input("Enter name of courier you wish to remove: ")
        removing_courier = removing_courier.title()
        removal_confirmation = int(input(
            "Is this correct '{}'? Enter 0 for yes and 1 for no: ".format(removing_courier)))
        if removal_confirmation == 0:
            if removing_courier in couriers:
                couriers.remove(removing_courier)
                print("Updated couriers list: ", couriers)
                update_couriers_txt()
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
        return  courier_menu()


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


def create_products_txt():
    f = open("Products_List.txt", "w+")

    for product in products:
        f.write(product + "\n")
    f.close()
    return read_products_txt()


def create_couriers_txt():
    f = open("Couriers_List.txt", "w+")

    for courier in couriers:
        f.write(courier + "\n")

    f.close()
    return read_couriers_txt()


def read_products_txt():
    f = open("Products_List.txt", "r")
    a = print(f.read())
    return a


def read_couriers_txt():
    f = open("Couriers_List.txt", "r")
    a =  print(f.read())
    return a


def update_products_txt():
    with open("Products_List.txt", "r+") as f:
        for product in products:
            f.write(product + "\n")
    f.close()
    contents = f.readlines()
    return contents


def update_couriers_txt():
    with open("Couriers_List.txt", "r+") as f:
        for courier in couriers:
            f.write(courier + "\n")
    f.close()
    contents = f.readlines()
    return contents


def checking_files_products():

    import os.path

    if os.path.isfile("Products_List.txt"):
        a = read_products_txt()
        return a

    else:
        b = create_products_txt()
        return b


def checking_files_couriers():

    import os.path

    if os.path.isfile("Couriers_List.txt"):
       return read_couriers_txt()

    else:
       return create_couriers_txt()


checking_files_products()
checking_files_couriers()
main_menu()


#unit tests
def test_read_couriers_txt():
    actual = read_couriers_txt()
    
    print(actual)
    expected = "Jack Johnson"

    assert actual == expected

# test_read_couriers_txt()

# def new():
#     with open(Products_List.txt, 'w+') as file:
        
# def exist():
#     import os.path
#     os.path.isfile(Couries_Lists.txt)
# try:
#     my_abs_path = my_file.resolve(strict=True)
# except FileNotFoundError:
#     return cre
# else:
#     # exists
