from datetime import datetime
from functions import *
from colorama import Fore, Back, Style, init
import json


class Shopping_Cart:
    def __init__(self):
        self.items = {}           
            
    def add_item(self, product, quantity):
        Clean()
        self.items[product.name] = {"price": product.price, "quantity": quantity}
        print(
            Fore.GREEN
            + f"[{product.name}] is added to the cart with quantity [{quantity}]"
            + Style.RESET_ALL
        )
        print("-" * (40 + len(product.name) + len(str(quantity))))
        return self.items[product.name]

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            Clean()
            print(
                Fore.YELLOW
                + f"[{item_name}] is removed from the cart"
                + Style.RESET_ALL
            )
            print("-" * (27 + len(item_name)))
        else:
            Clean()
            print(Fore.RED + f"--{item_name}-- is not in the cart" + Style.RESET_ALL)
        return self.items

    def update_quantity(self, item_name, new_quantity, quantity):
        Clean()
        if not self.items:
            Clean()
            print("There are no items in the cart")
        elif item_name in self.items:
            self.items[item_name]["quantity"] = new_quantity
            print(
                Fore.GREEN
                + f"[{item_name}] quantity is updated from [{quantity}] to [{new_quantity}]"
                + Style.RESET_ALL
            )
        else:
            Clean()
            print(Fore.RED + "There are no items in the cart" + Style.RESET_ALL)
        return self.items

    def calculate_total(self):
        total = 0
        for item_name in self.items:
            total += self.items[item_name]["price"] * self.items[item_name]["quantity"]
        return total

    def calc_number_of_items(self):
        return len(self.items)

    def display_items(self):
        return self.items


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_product_info(self):
        return f"Product Name: {self.name}, Price: {self.price}"

    def __str__(self):
        return self.name


class Receipt:
    def __init__(self, cart, customer_name):
        self.cart = cart
        self.customer_name = customer_name
        self.total_price = cart.calculate_total()
        self.number_of_items = cart.calc_number_of_items()
        self.display_receipt()

    def display_receipt(self):
        print(Fore.CYAN + "Receipt" + Style.RESET_ALL)
        print(Fore.MAGENTA + "---" * 10 + Style.RESET_ALL)
        print(
            Fore.YELLOW
            + f"Date: {datetime.now().strftime('%Y-%m-%d')}"
            + Style.RESET_ALL
        )
        print(Fore.YELLOW + f"Customer: {self.customer_name}" + Style.RESET_ALL)
        print(Fore.MAGENTA + "---" * 10 + Style.RESET_ALL)
        print(Fore.GREEN + "Product\t\tQuantity\tPrice" + Style.RESET_ALL)

        for item_name, item_info in self.cart.items.items():
            print(
                Fore.BLUE
                + f"{item_name}\t\t{item_info['quantity']}\t\t{item_info['price']}"
                + Style.RESET_ALL
            )

        print(Fore.MAGENTA + "---" * 10 + Style.RESET_ALL)
        print(Fore.RED + f"Total Price: {self.total_price}" + Style.RESET_ALL)
        print(Fore.CYAN + f"Number of Items: {self.number_of_items}" + Style.RESET_ALL)
        print(Fore.MAGENTA + "---" * 10 + Style.RESET_ALL)




def testing():
    cart = Shopping_Cart()

    apple = Product("Apple", 1.5)
    cart.add_item(apple, 5)

    banana = Product("Banana", 0.8)
    cart.add_item(banana, 3)

    print(cart.display_items())  # Output cart items

    print(f"Total Price: {cart.calculate_total()}")  # Calculate total price
    print(
        f"Number of Items: {cart.calc_number_of_items()}"
    )  # Calculate number of items

    cart.update_quantity("Apple", 10)
    print(cart.display_items())  # Update quantity of apples

    cart.remove_item("Banana")
    print(cart.display_items())  # Remove bananas

    receipt = Receipt(cart, "John Doe")


# testing()
