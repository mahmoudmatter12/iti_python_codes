from random import randint
from time import time
import os
from colorama import Fore, Back, Style, init



def average_in_list(lst):
    return sum(lst) / len(lst)


def generate_random_numbers():
    with open("numbers.dat", "a") as file:
        random_numbers = [randint(1, 100) for _ in range(20)]
        for num in random_numbers:
            file.write(f"{num}\n")
    return None


#!===========================================================
#! lab 1
def calc_time(inner_time):
    def wrap(*args, **kwargs):
        start = time()
        inner_time(*args, **kwargs)
        end = time()
        print("Function time is", end - start, "s")

    return wrap


#!===========================================================
def clear_file(filename):
    with open(filename, "w") as file:
        file.write("")
        print(f"File {filename} cleared")


def Greeting_Customer(name):
    print(Fore.MAGENTA + f"Hello {name}, Welcome to our store"+ Style.RESET_ALL)
    print("-" * (28 + len(name)))


def Clean():
    os.system("cls" if os.name == "nt" else "clear")
