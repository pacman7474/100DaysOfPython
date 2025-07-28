from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


my_coffee_machine = CoffeeMaker()
my_money_machine = MoneyMachine()
coffee_menu = Menu()

machine_running = True

while machine_running:
    print("Welcome to our coffee machine")
    selection = input(f"Please choose from the following: {coffee_menu.get_items()}: ")
    if selection == "report":
        my_coffee_machine.report()
        my_money_machine.report()
    elif selection == "off":
        machine_running = False
    else:
        item = coffee_menu.find_drink(selection)
        if item:
            if my_coffee_machine.is_resource_sufficient(item):
                if my_money_machine.make_payment(item.cost):
                    my_coffee_machine.make_coffee(item)


