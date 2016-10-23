# saved other code as a separate module (transactions.py) to import
import promotion
import storecard
from transactions import *
from promotion import *
from storecard import *

items = ["DONUT", "LATTE", "FILTER", "MUFFIN"]
prices = [1.5, 2.0, 1.80, 1.20]
running = True

while running:
    option_number = 1
    for item in items:
        print(str(option_number) + ". " + item)
        option_number += 1

    print(str(option_number) + ". Quit")
    end_program_option = option_number
    choice = int(input("Choose an option: "))
    if choice == end_program_option:
        running = False
    else:
        store_card = input("Do you have a store card? Y/N: ")
        credit_card = input("Credit card number: ")
        new_price = promotion.discount(prices[choice - 1])
        if store_card == "Y":
            new_price = storecard.discount(new_price)
        save_transaction(new_price, credit_card, items[choice - 1])
