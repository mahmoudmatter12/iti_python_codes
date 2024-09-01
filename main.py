from classes import *
from functions import *
from colorama import Fore, Back, Style, init



def main():
    Clean()
    cart = Shopping_Cart()
    name = input(Fore.YELLOW + "Enter Customer Name: " + Style.RESET_ALL).capitalize()
    Clean()
    Greeting_Customer(name)
    while True:
        print(Fore.LIGHTCYAN_EX + "1. Add Item" + Style.RESET_ALL)
        print(Fore.LIGHTCYAN_EX + "2. Remove Item" + Style.RESET_ALL)
        print(Fore.LIGHTCYAN_EX + "3. Update Quantity" + Style.RESET_ALL)
        print(Fore.LIGHTCYAN_EX + "4. Calculate Total" + Style.RESET_ALL)
        print(Fore.LIGHTCYAN_EX + "5. Number of Items" + Style.RESET_ALL)
        print(Fore.LIGHTCYAN_EX + "6. Display Items" + Style.RESET_ALL)
        print(Fore.LIGHTCYAN_EX + "7. Clear Cart" + Style.RESET_ALL)
        print(Fore.LIGHTCYAN_EX + "8. Display Receipt" + Style.RESET_ALL)
        print(Fore.LIGHTCYAN_EX + "9. Exit" + Style.RESET_ALL)
        choice = int(input(Fore.CYAN + "Enter your choice: " + Style.RESET_ALL))

        while choice not in range(1, 10):
            choice = int(
                input(
                    Fore.RED + "Invalid Choice, Enter your choice from 1..9: " + Style.RESET_ALL
                )
            )

        if choice == 1:
            Clean()
            name = input(
                Fore.YELLOW + "Enter Product Name: " + Style.RESET_ALL
            ).capitalize()
            while not name.isalpha():
                name = input(
                    Fore.RED + "Invalid name, Enter Product name: " + Style.RESET_ALL
                )
            price = input(Fore.YELLOW + "Enter Product Price: " + Style.RESET_ALL)
            while True:
                try:
                    price = float(price)
                    if price < 0:
                        raise ValueError
                    break
                except ValueError:
                    price = input(
                        Fore.RED
                        + "Invalid price, Enter Product Price: "
                        + Style.RESET_ALL
                    )
            quantity = int(
                input(Fore.YELLOW + "Enter Product Quantity: " + Style.RESET_ALL)
            )
            while True:
                try:
                    quantity = int(quantity)
                    if quantity < 0:
                        raise ValueError
                    break
                except ValueError:
                    quantity = input(
                        Fore.RED
                        + "Invalid quantity, Enter Product quantity: "
                        + Style.RESET_ALL
                    )
            product = Product(name, price)
            cart.add_item(product, quantity)
            

        elif choice == 2:
            Clean()
            item_name = input(
                Fore.YELLOW + "Enter Item Name: " + Style.RESET_ALL
            ).capitalize()
            cart.remove_item(item_name)

        elif choice == 3:
            Clean()
            if not cart.items:
                Clean()
                print(Fore.RED + "Cart is empty \n" + Style.RESET_ALL)
                continue
            else:
                item_name = input(
                    Fore.YELLOW + "Enter Item Name: " + Style.RESET_ALL
                ).capitalize()
                while True:
                    try:
                        new_quantity = int(
                            input(
                                Fore.YELLOW + "Enter New Quantity: " + Style.RESET_ALL
                            )
                        )
                        if new_quantity < 0:
                            raise ValueError("Quantity cannot be negative")
                        break
                    except ValueError:
                        print(
                            Fore.RED
                            + "Invalid quantity, please enter a non-negative integer."
                            + Style.RESET_ALL
                        )
                cart.update_quantity(
                    item_name, new_quantity, cart.items[item_name]["quantity"]
                )

        elif choice == 4:
            Clean()
            print(
                Fore.CYAN
                + f"The Total Price for {cart.calc_number_of_items()} items is {cart.calculate_total()} \n"
                + Style.RESET_ALL
            )

        elif choice == 5:
            Clean()
            print(
                Fore.YELLOW
                + f"Number of Items: {cart.calc_number_of_items()} \n"
                + Style.RESET_ALL
            )

        elif choice == 6:
            Clean()
            if not cart.items:
                print(Fore.RED + "Cart is empty" + Style.RESET_ALL)
            else:
                print(Fore.GREEN + f"{cart.display_items()}" + Style.RESET_ALL)

        elif choice == 7:
            Clean()
            cart.items = {}
            print(Fore.RED + "Cart is cleared" + Style.RESET_ALL)

        elif choice == 8:
            Clean()
            receipt = Receipt(cart, name)
            break

        elif choice == 9:
            Clean()
            print(Fore.GREEN + "Thank you for shopping with us" + Style.RESET_ALL)
            break


main()


# mahmoodgamal045@gmail.com