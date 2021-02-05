products = ["Coke", "Pepsi"]

def main_menu():
    print("Main Menu\n")
    print("To exit app enter 0")
    print("To go to Product Menu enter 1")
    input1 = int(input("Where to: "))
    try:
        if input1 == 0:
            print("Exiting App")
            return exit
        elif input1 == 1:
            print("\nProduct Menu\n")
            return product_menu()
        else:
            print("\nInvalid Input!\n")
            return main_menu()
    except ValueError:
        print("\nInvalid Input. Returning to main menu.\n")
        return main_menu()


def product_menu():
    print("To return to Main Menu enter 0")
    print("To view products enter 1")
    print("To add a new product enter 2")
    print("To add a update product enter 3")
    print("To remove a product enter 4")
    input2 = int(input("Where to: "))
    try:
        if input2 == 0:
            return return_to_main()
        elif input2 == 1:
            return view_products()
            # print("View Products")
            # # # product_list()
            # # print(products)
            # # product_menu()
        elif input2 == 2:
            return add_new_product()
            # print("Create new product")
            # new_product = input("Enter name of new product: ")
            # new_product = new_product.title()
            # print("{} has been added to product list".format(new_product))
            # products.append(new_product)
            # print(products)
            # product_menu()
        elif input2 == 3:
            return update_product()
            # updating_product = input("Enter name of product you wish to update: ")
            # updating_product = updating_product.title()
            # confirmation_update = int(input(
            #     "Is this correct '{}'? Enter 0 for yes and 1 for no: ".format(updating_product)))
            # if confirmation_update == 1:
            #     print("Returning to product menu")
            #     product_menu()
            # elif confirmation_update == 0:
            #     if updating_product in products:
            #         updated_product = input("Replace product with: ")
            #         updated_product = updated_product.title()
            #         update_confirmation = int(input(
            #             "Is this correct '{}'? Enter 0 for yes and 1 for no: ".format(updated_product)))
            #         if update_confirmation == 0:
            #             index = products.index(updating_product)
            #             products.insert(index, updated_product)
            #             products.remove(updating_product)
            #             print("Here is an updated product list: ",
            #                   products, "Returnig to product menu ")
            #             product_menu()

            #         elif update_confirmation == 1:
            #             print("Returning to product menu")
            #             product_menu()
            #         else:
            #             print("Invalid input! Returning to product menu")
            #             product_menu()
            #     else:
            #         print("\nThat Product does not exist!\nReturning to product menu")
            #         product_menu()

            # else:
            #     print("\nInvalid Entry! Returning to product menu\n")
        elif input2 == 4:
            return remove_product()
            # removing_product = input("Enter name of product you wish to remove: ")
            # removing_product = removing_product.title()
            # removal_confirmation = int(input(
            #     "Is this correct '{}'? Enter 0 for yes and 1 for no: ".format(removing_product)))
            # if removal_confirmation == 0:
            #     if removing_product in products:
            #         products.remove(removing_product)
            #         print("Updated product list: ", products)
            #         product_menu()
            #     else:
            #         print(
            #             "That item is not in the products list. Returning to product menu.")
            #         product_menu()
            # elif removal_confirmation == 1:
            #     print("Returning to product menu")
            #     product_menu()
            # else:
            #     print("Invalid input! Returning to product menu")
            #     product_menu()
        else:
            print("Invalid Input!")
            return product_menu()
    except ValueError:
        error_meassge = print("Invalid Input! Returning to product menu.\n")
        return error_meassge

def return_to_main():
    print("Return to Main Menu")
    return main_menu()

def view_products():
    print("\nProducts:\n")
    open_this()
    return product_menu()

def add_new_product():
    print("Add new product")
    new_product = input("Enter name of new product: ")
    new_product = new_product.title()
    print("{} has been added to product list".format(new_product))
    products.append(new_product)
    print("PRINTING: " , products)
    save_file()
    open_this()
    return product_menu()

def update_product():
    updating_product = input("Enter name of product you wish to update: ")
    updating_product = updating_product.title()
    confirmation_update = int(input(
        "Is this correct '{}'? Enter 0 for yes and 1 for no: ".format(updating_product)))
    if confirmation_update == 1:
        print("Returning to product menu")
        return product_menu()
    elif confirmation_update == 0:
        if updating_product in products:
            updated_product = input("Replace product with: ")
            updated_product = updated_product.title()
            update_confirmation = int(input(
                "Is this correct '{}'? Enter 0 for yes and 1 for no: ".format(updated_product)))
            if update_confirmation == 0:
                index = products.index(updating_product)
                products.insert(index, updated_product)
                products.remove(updating_product)
                # print("Here is an updated product list: ",products, "\nReturnig to product menu\n")
                save_file()
                open_this()
                return product_menu()

            elif update_confirmation == 1:
                print("Returning to product menu")
                return product_menu()
            else:
                print("Invalid input! Returning to product menu")
                return product_menu()
        else:
            print("\nThat Product does not exist!\nReturning to product menu")
            return product_menu()

    else:
        print("\nInvalid Entry! Returning to product menu\n")
        return product_menu()

def remove_product():
    print(products)
    removing_product = input("Enter name of product you wish to remove: ")
    removing_product = removing_product.title()
    removal_confirmation = int(input(
        "Is this correct '{}'? Enter 0 for yes and 1 for no: ".format(removing_product)))
    if removal_confirmation == 0:
        if removing_product in products:
            products.remove(removing_product)
            # print("Updated product list: ", products)
            save_file()
            open_this()
            return product_menu()
        else:
            print("That item is not in the products list. Returning to product menu\n.")
            return product_menu()
    elif removal_confirmation == 1:
        print("Returning to product menu")
        return product_menu()
    else:
        print("Invalid input! Returning to product menu")
        return product_menu()


def save_file():
    with open("product list.txt", "w+") as product_file:
        for product in products:
            product_file.write(product + "\n")

# def open_file():
#     import os.path

#     if os.path.isfile("product list.txt"):
#         product_file = open("product list.txt", "r")
#         lines = product_file.readlines()
#         for line in lines:
#             return line
#         product_file.close()

#     else:
#         save_file()
#         return open_file()
        
def open_this():
    try:
        import os.path

        if os.path.isfile("product list.txt"):
            product_file = open("product list.txt", "r+")
            print("IF")

        else:
            product_file = open("product list.txt", "w+")
            for line in product_file.readlines():
                products.append(line)
                # product_file.writelines(product + "\n")
            print("ELSE")

        contents = product_file.read()
        return contents

        

    except FileNotFoundError as fnfe:
        print('Unable to open file: ' + str(fnfe))
        
    except Exception as e:
        print('An error occurred: ' + str(e))

    finally:
        product_file.close()


# open_file()
open_this()
main_menu()

