'''
project needs
1. print a report of resources and money
2. check if there are enough resources to make desired product.
3. process coin payment (penny-quarters.)
4. check if payment is enough for desired product.
5. make the coffee.
'''

#global variables
bank = 0.0
order = 0.0
cont = True
payment = []
#constant dictionary
MENU = {
    "espresso":{
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
    "cost": 1.5,
    },
    "latte": {
        "ingredients":{
        "water": 200,
        "coffee": 24,
        "milk": 150
        },
    "cost":2.50
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100
        },
        "cost": 3.00
    }

}

COINS = {
    "penny":0.01,
    "nickel":0.05,
    "dime":0.1,
    "quarter":0.25

}
resources = {
    "water":300,
    "milk": 200,
    "coffee":100
}


#functions

#this calculates how much customer is paying
def pay():
    quarters = int(input("how many quarters: "))
    payment.append(round((quarters * COINS['quarter']), 2))
    dimes = int(input("how many dimes: "))
    payment.append(round((dimes * COINS['dime']), 2))
    nickels = int(input("how many nickels: "))
    payment.append(round(nickels * COINS['nickel'], 2))
    pennies = int(input("how many pennies: "))
    payment.append(round(pennies * COINS['penny'], 2))

def espresso():
    global bank
    if resources['water'] > MENU['espresso']['ingredients']['water']:
        print("your coffee was made")
        bank += order
        resources['water'] -= MENU['espresso']['ingredients']['water']
        print(resources['water'])
        print(bank)
def latte():
    print("filler")

def cappuccino():
    print("filler")
'''
ask what they want DONE
store value DONE
if user enters report display remaining resources and money earned.
prompt user to insert coins
user inputs coins
check if amount inputed by user is enough for desired drink 
if not refund and ask again
if enough give coffee and subtract from total resources while adding to money total
if not enough resources display lack of x material 
'''
#project begin
while cont:
    userI = input("what would you like to order (espresso/latte/cappuccino) ").lower()

    if userI == "report":
        print(f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml"
              f"\nCoffee: {resources['coffee']}g \nMoney: ${bank}")
    else:
        pay()
        for i in range(len(payment)):
            order += payment[i]
        if userI == "espresso":
            espresso()
        elif userI == "latte":
            latte()
        elif userI == "cappuccino":
            cappuccino()







