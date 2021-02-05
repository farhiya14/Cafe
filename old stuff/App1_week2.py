products = ["Coke", "Coke Zero", "Fanta Orange", "Water", "Coffee"]

couriers = ["Jack Johnson", "Doctor Who", "Farhiya Nur"]

def Main_Menu():
    print("\nMain Menu")
    print("\nTo exit app enter 0")
    print("To go to Product Menu enter 1")
    print("To go to Courier Menu enter 2")
    input1 = int(input("Where to: "))
    if input1 == 0:
        print("Exiting App")
        return exit
    elif input1 == 1:
        print("\nProduct Menu\n")
        return product_menu()
    elif input1 == 2:
        print("\nCourier Menu\n")
        return Courier_Menu()
    else:
        print("Invalid Input!")
        return Main_Menu()


def return_to_main_menu():
    print("Return to Main Menu")
    return Main_Menu()

def view_products():
    return read_Products_txt() 

def add_new_product():
    read_Products_txt()
    print("\nAdd a new product\n")
    global new_product
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
            print("{} has been added to product list\n".format(new_product))
            products.append(new_product)
            # print(products, "\nReturning to product menu")
            # update_Products_txt()
            add_products_to_txt()
            read_Products_txt()
            return product_menu()
    elif confirmation == 1:
        print("Returning to product menu\n")
        return product_menu()
    else:
        print("Invalid input! Returning to product menu")
        return product_menu()

def update_product():
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
                print("Here is an updated product list: ", read_Products_txt(), "\nReturnig to product menu ")
                update_Products_txt()
                # read_Products_txt()
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
        removing_product = input("Enter name of product you wish to remove: ")
        removing_product = removing_product.title()
        removal_confirmation = int(input(
            "Is this correct '{}'? Enter 0 for yes and 1 for no: ".format(removing_product)))
        if removal_confirmation == 0:
            if removing_product in products:
                products.remove(removing_product)
                # print("Updated product list: ", products)
                update_Products_txt()
                read_Products_txt()
                return product_menu()
            else:
                print(
                    "That item is not in the products list. Returning to product menu.")
                return product_menu()
        elif removal_confirmation == 1:
            print("Returning to product menu")
            return product_menu()
        else:
            print("Invalid input! Returning to product menu")
            return product_menu()


def product_menu():
    print("\nTo return to Main Menu enter 0")
    print("To view products enter 1")
    print("To add a new product enter 2")
    print("To update a product enter 3")
    print("To remove a product enter 4")
    input2 = int(input("Where to: "))
    
    try:
        if input2 == 0:
            return return_to_main_menu()
        elif input2 == 1:
            view_products()
            return product_menu()
        elif input2 == 2:
            return add_new_product()
            # print("Create new product")
            # new_product = input("Enter name of new product: ")
            # new_product = new_product.title()
            # confirmation = int(
            #     input("Is this correct '{}'? Enter 0 for yes and 1 for no: ".format(new_product)))
            # if confirmation == 0:
            #     if new_product in products:
            #         print("{} is already in the list.\nReturning to product menu".format(
            #             new_product))
            #         return product_menu()
            #     else:
            #         print("{} has been added to product list".format(new_product))
            #         products.append(new_product)
            #         print(products, "\n Returning to product menu")
            #         update_Products_txt()
            #         product_menu()
            # elif confirmation == 1:
            #     print("Returning to product menu")
            #     product_menu()
            # else:
            #     print("Invalid input! Returning to product menu")
            #     product_menu()
        elif input2 == 3:
            return update_product()
            # updating_product = input("Enter name of product you wish to update: ")
            # updating_product = updating_product.title()
            # confirmation_update = int(input(
            #     "Is this correct '{}'? Enter 0 for yes and 1 for no: ".format(updating_product)))
            # if confirmation_update == 1:
            #     print("\nReturning to product menu")
            #     product_menu()
            # elif confirmation_update == 0:
            #     if updating_product in products:
            #         updated_product = input("Replace product with: ")
            #         updated_product = updated_product.title()
            #         update_confirmation = int(input(
            #             "Is this correct '{}'? Enter 0 for yes and 1 for no: ".format(updated_product)))
            #         if update_confirmation == 0:
            #             index = products.index(updating_product)
            #             products.remove(updating_product)
            #             products.insert(index, updated_product)
            #             print("Here is an updated product list: ",
            #                   products, "\nReturnig to product menu ")
            #             update_Products_txt()
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
            #         update_Products_txt()
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
            product_menu()
    except ValueError:
        print("Invalid input! Try again!\n")
        return product_menu()


def Courier_Menu():
    print("To return to Main Menu enter 0")
    print("To view couriers enter 1")
    print("To add a new courier enter 2")
    print("To add a update courier enter 3")
    print("To remove a courier enter 4")
    input3 = int(input("Where to: "))

    if input3 == 0:
        print("Return to Main Menu")
        print("Main Menu")
        Main_Menu()
    elif input3 == 1:
        print("Couriers:")
        read_Couriers_txt()
        Courier_Menu()
    elif input3 == 2:
        print("Create new courier")
        new_courier = input("Enter name of new courier: ")
        new_courier = new_courier.title()
        confirmation = int(
            input("Is this correct '{}'? Enter 0 for yes and 1 for no: ".format(new_courier)))
        if confirmation == 0:
            if new_courier in couriers:
                print("{} is already in the list.\nReturning to product menu".format(
                    new_courier))
                return Courier_Menu()
            else:
                print("{} has been added to couriers list".format(new_courier))
                couriers.append(new_courier)
                print(couriers)
                update_Couriers_txt()
                Courier_Menu()
        elif confirmation == 1:
            print("Returning to courier menu")
            Courier_Menu()
        else:
            print("Invalid input! Returning to courier menu")
            Courier_Menu()
    elif input3 == 3:
        updating_courier = input("Enter name of courier you wish to update: ")
        updating_courier = updating_courier.title()
        confirmation_update = int(input(
            "Is this correct '{}'? Enter 0 for yes and 1 for no: ".format(updating_courier)))
        if confirmation_update == 1:
            print("Returning to courier menu")
            Courier_Menu()
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
                    update_Couriers_txt()
                    Courier_Menu()

                elif update_confirmation == 1:
                    print("Returning to couriers menu")
                    Courier_Menu()
                else:
                    print("Invalid input! Returning to couriers menu")
                    Courier_Menu()
            else:
                print("\nThat courier does not exist!\nReturning to couriers menu")
                Courier_Menu()

        else:
            print("\nInvalid Entry! Returning to couriers menu\n")
    elif input3 == 4:
        removing_courier = input("Enter name of courier you wish to remove: ")
        removing_courier = removing_courier.title()
        removal_confirmation = int(input(
            "Is this correct '{}'? Enter 0 for yes and 1 for no: ".format(removing_courier)))
        if removal_confirmation == 0:
            if removing_courier in couriers:
                couriers.remove(removing_courier)
                print("Updated couriers list: ", couriers)
                update_Couriers_txt()
                Courier_Menu()
            else:
                print(
                    "That item is not in the couriers list. Returning to courier menu.")
                Courier_Menu()
        elif removal_confirmation == 1:
            print("Returning to couriers menu")
            Courier_Menu()
        else:
            print("Invalid input! Returning to couriers menu")
            Courier_Menu()
    else:
        print("Invalid Input!")
        Courier_Menu()


def Create_Products_txt():
    product_file = open("Products_List.txt", "w+")

    for product in products:
        product_file.write(product + " \n")

    product_file.close()

    return read_Products_txt()
 

def Create_Couriers_txt():
    courier_file = open("Couriers_List.txt", "w+")

    for courier in couriers:
        courier_file.write(courier + " \n")

    courier_file.close()

    return read_Couriers_txt()


def read_Products_txt():
    with open("Products_List.txt", "r") as product_file:
        contents = print(product_file.read())
    # file.close()
    return contents


def read_Couriers_txt():
    # f = open("Couriers_List.txt", "r")
    # print(f.read())
    with open("Couriers_List.txt", "r") as courier_file:
        contents = print(courier_file.read())
    # file.close()
    return contents

def add_products_to_txt():
    product_file = open("Products_List.txt", "a")
    # for product in products:
    #     file.write(product + "\n")
    product_file.write("{}\n".format(new_product))
    product_file.close  

def update_Products_txt():
    with open("Products_List.txt", "w+") as product_file:
        for product in products:
            product_file.write(product + "\n")
    return products

    # file = open("Products_List.txt", "w+")
    # for product in products:
    #     file.write(product + "\n")
    # file.close()


    


def update_Couriers_txt():
    with open("Couriers_List.txt", "w+") as courier_file:
        for courier in couriers:
            courier_file.write(courier + "\n")
    # f.close()
    return couriers


def checking_files_products():

    import os.path

    if os.path.isfile("Products_List.txt"):
        return read_Products_txt()

    else:
        return Create_Products_txt()


def checking_files_couriers():

    import os.path

    if os.path.isfile("Couriers_List.txt"):
        return read_Couriers_txt()

    else:
        return Create_Couriers_txt()


checking_files_products()
checking_files_couriers()
# read_Products_txt()
# read_Couriers_txt()
Main_Menu()
