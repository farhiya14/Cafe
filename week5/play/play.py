

couriers = [{"id": 1,
             "name": "Jack",
             "phone number": "7418529966375"},
            {"id": 2,
             "name": "Tom",
             "phone number": "01478523695"}]






# def choose_a_courier(courier_picked):

#     for i, courier in enumerate(couriers):
#         i += 1
#         print(i, courier)

#     # load_file_couriers()

#     # global chosen_courier

#     try:
#         courier_picked = int(
#             input("\nPlease choose a courier from the list above: "))

#         if courier_picked == 0:
#             print("choose from the list")
#             return choose_a_courier(courier_picked)

#         courier_picked -= 1

#         print(couriers[courier_picked])

#         return couriers[courier_picked]

#         # un comment if you want to sort orders my courier
#         # chosen_courier = str(chosen_courier)

#         # chosen_courier += 1

#     except ValueError:
#         print("invalid input")
#         return choose_a_courier(courier_picked)

#     except IndexError:
#         print("invalid input")
#         return choose_a_courier(courier_picked)


# # choose_a_courier(courier_picked)

# # for order in orders:
# #     if order == selected_order:
# #         selected_order["courier"] = couriers[choose_a_courier(courier_picked)]["id"]









# for i, courier in enumerate(couriers):
#     i += 1
#     print(i, courier)



# def func(picked):

#     picked -= 1

#     return couriers[picked]

# picked_courier = int(input("select a courier from the list: "))

# new = func(picked_courier)
# # print(new)


# def func2():
#     picked_courier = input("select a courier from the list: ")

#     try:
#         if picked_courier != "":
#             picked_courier = int(picked_courier)
#             new_c = app.func(picked_courier)

#             for order in app.orders:
#                 if order == app.selected_order:
#                     app.selected_order["courier"] = new_c["id"]

#     except IndexError:
#         print("wrong index")
#         return func2()

