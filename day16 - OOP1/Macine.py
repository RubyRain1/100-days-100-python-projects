from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cont = True
menu = Menu()
report = CoffeeMaker()
money = MoneyMachine()

def report_print():
    return report.report(), money.report()

def make_coffe():
    report.make_coffee(userI)
while cont:
    userI = input("what would you like? (espresso/latte/cappuccino): ")
    if userI == "report":
        report_print()
    elif userI == "latte":
        make_coffe()
    elif userI == "espresso":
        print("espresso")


