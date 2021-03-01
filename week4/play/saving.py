def get_product():
    load_file_products()

    try:
        selected = int(input("select product or 0 to cancel: "))
        if selected == 0:
            print("\nReturning to Product menu\n")
            return product_menu()

        selected -= 1

        global selected_product

        selected_product = products[selected]
        print("\n", selected_product)

    except ValueError:
        print("Invalid entry\nReturning to Product menu")
        return product_menu()

    except IndexError:
        print("\nInvalid entry\nTry again")
        return product_menu()
    try:
        if input2 == 3:
            return update_products()
        elif input2 == 4:
            return removal_of_product()
    except ValueError:
        print("\nInvalid input\n")
        return product_menu()
