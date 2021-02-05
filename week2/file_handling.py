
# def load_file_products():
#     my_file = open("products list.txt", "r")
#     contents = print(my_file.read())
#     return contents

# def load_file_couriers():
#     my_file = open("couriers list.txt", "r")
#     contents = print(my_file.read())
#     return contents

# def add_new_product_file():
#     my_file = open("products list.txt", "a")
#     my_file.write(new_product)
#     my_file.close()


# def add_new_courier_file():
#     my_file = open("couriers list.txt", "a")
#     my_file.write(app.new_courier)
#     my_file.close()

# def save_updated_products():
#     my_file = open("products list.txt", "w+")
#     for product in products:
#         my_file.write(product, "\n")
#     my_file.close
# def save_updated_couriers():
#     my_file = open("couriers list.txt", "w+")
#     for courier in couriers:
#         my_file.write(courier, "\n")
#     my_file.close

# def checkin_file_existance_products():
#     import os.path

#     if os.path.isfile("products list.txt"):
#         return load_file_products()
#     else:
#         save_updated_products()
#         load_file_couriers()
# def checkin_file_existance_couriers():
#     import os.path

#     if os.path.isfile("couriers list.txt"):
#         return load_file_couriers()
#     else:
#         save_updated_couriers()
#         load_file_couriers()