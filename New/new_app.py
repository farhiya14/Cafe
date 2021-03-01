import os

def main_menu():
    print("\nMain Menu")
    print("\nTo exit app enter 0")
    print("To go to Product Menu enter 1")
    print("To go to Courier Menu enter 2")
    print("To go to Order Menu enter 3")
    input1 = int(input("Where to: "))
    from products import product_menu
    try:
        if input1 == 0:
            print("Exiting App")
            return quit()
        elif input1 == 1:
            return product_menu()
        elif input1 == 2:
            from couriers import courier_menu
            return courier_menu()
        elif input1 == 3:
            from orders import order_menu
            return order_menu()
        else:
            print("\nInvalid Input!")
            return main_menu()
    except ValueError:
        print("\nInvalid Input!")
        return main_menu()

    os.system('clear')

def stuff():
    from products import checking_file_existance_products
    from couriers import checking_file_existance_couriers
    from orders import checking_file_existance_orders

    checking_file_existance_products()
    checking_file_existance_couriers()
    checking_file_existance_orders()

    main_menu()


# main_menu()

stuff()