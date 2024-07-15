from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cont = True
menu = Menu()
report = CoffeeMaker()
money = MoneyMachine()

while cont:
    options = menu.get_items()
    userI = input(f"what would you like? {options}: ")
    if userI == "n":
        cont = False
    elif userI == "report":
        report.report()
        money.report()
    else:
        drink = menu.find_drink(userI)

        if report.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            print(f"here is your {options}")
        else:
            "we cannot make the requested drink"
