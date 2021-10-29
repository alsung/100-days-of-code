# Day 16 Coffee Machine OOP Project

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
coffee_machine = CoffeeMaker()
money_maker = MoneyMachine()

while is_on:

    choice = input(" What would you like? (espresso/latte/cappuccino): ")

    if choice == "off":
        print("Goodbye!")
        is_on = False
    elif choice == "report":
        coffee_machine.report()
        money_maker.report()