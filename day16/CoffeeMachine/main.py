# Day 16 Coffee Machine OOP Project

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


# TODO 2: Check resources sufficient?
    # coffee_maker.py
# TODO 3: Process coins
# TODO 4: Check transation successful?
# TODO 5: Make coffee.

is_on = True
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()


while is_on:
    options = menu.get_items()
    choice = input(f" What would you like? ({options}): ")

    if choice == "off":
        print("Goodbye!")
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)