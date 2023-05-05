# class ShoppingCart:
#
#     def __init__(self):
#         self.data = {}
#
#     def add(self):
#         i = input("What would you like to add to your cart? ")
#         self.data[i] = input("Quantity: ")
#
#     # def show(self):
#     #     print("The content of the shopping cart are:")
#     #
#     #     for state, capital in data.items():
#     #         print(state, ":", capital)
#
#     def clear(self):
#         if input("Clear your list? [y/n] ").lower().startswith("y"):
#             self.data = {}
#             print("Your list has been cleared.")
#         else:
#             print("Action abandoned.")
#
#     def delete(self):
#         print("Still working on that, use 'clear' for now please.")
#
#
#
#     def menu_loop(self):
#         while True:
#             i = input(
#                 "Make your shopping list. "
#                 "Please type (Add/Delete/Clear/Quit). "
#             ).lower()
#             if i == "quit":
#                 break
#             try:
#                 getattr(self, i)()
#             except AttributeError:
#                 print(
#                     'Oops! Something went wrong. '
#                     'Please type "(Show/Add/Delete/Clear/Quit)"'
#                 )
#
# cart = ShoppingCart()
# cart.menu_loop()
# print(cart.data)


def menu():
    print("1. Add a new item")
    print("2. Display the content of the shopping cart")
    print("3. Remove an item of the shopping cart")
    print("4. Compute total of the items in the shopping cart")
    print("5. Quit")


def add_item():
    name = input("What item would you like to add? ")
    price = float(input(f"What is the price of the {name}? "))
    cart.append([name, price])
    print(f"{name} has been added to the cart.")


def display_content():
    print("The content of the shopping cart are:")

    for name, price in cart:
        print(f"{name} - {price}")


def remove_item():
    selected_name = input("Which item would you like to remove? ")
    temp = []
    for name, price in cart:
        if name != selected_name:
            temp.append([name, price])
    cart = temp


def total_sum():
    summation = 0

    for name, price in cart:
        summation += price

    print(f'The total price of the items in the shopping cart is ${summation}')

def menu_loop(self):
        while True:
            i = input(
                "Make your shopping list. "
                "Please type (Show/Add/Delete/Clear/Quit). "
            ).lower()
            if i == "quit":
                break
            try:
                getattr(self, i)()
            except AttributeError:
                print(
                    'Oops! Something went wrong. '
                    'Please type "(Show/Add/Delete/Clear/Quit)"'
                )



cart = []

print("Welcome to the Shopping Cart Program!")
print()

while True:

    menu()
    option = int(input("Please, enter an action: "))

    if option == 5:
        break

    elif option == 1:
        add_item()

    elif option == 2:
        display_content()

    elif option == 3:
        remove_item()

    elif option == 4:
        total_sum()

    else:
        print("Invalid option, please, try again.")

print("Thank you for using the shopping cart program. Good bye!")