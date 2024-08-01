
#global variables
bank = 0.0
order = 0.0
change = 0.0
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
    "coffee": 100
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

#this is the latte calculations for orders
def latte():
    global bank
    global change
    if order < MENU['latte']['cost']:
        print(f"you paid {order} the price of a latte is {MENU['latte']['cost']},\n"
              f"please order again")
    elif resources['water'] < MENU['latte']['ingredients']['water']:
        print("we are out of water, here is a refund. Please order again.")
    elif resources['milk'] < MENU['latte']['ingredients']['milk']:
        print("we are out of milk, here is a refund. Please order again.")
    elif resources['coffee'] < MENU['latte']['ingredients']['coffee']:
        print("we are out of coffee beans, here is a refund. Please order again!")
    else:
        print("your latte was made")
        bank += MENU['latte']['cost']
        resources['water'] -= MENU['latte']['ingredients']['water']
        resources['coffee'] -= MENU['latte']['ingredients']['coffee']
        resources['milk'] -= MENU['latte']['ingredients']['milk']
        print(f"Here is your change: ${round(change, 2)}")

#this is the espresso calculations for orders
def espresso():
    global bank #have to modify global variable.
    global change
    #check if there are enough resources and subracts from total resources.
    if order < MENU['espresso']['cost']:
        print(f"you paid {order}, the cost of an espresso is {MENU['espresso']['cost']}\n"
              f"please order again.")
    elif resources['water'] < MENU['espresso']['ingredients']['water'] :
        print("we are out of water, here is a refund. Please order again.")
    elif resources['coffee'] < MENU['espresso']['ingredients']['coffee']:
        print("we are out of coffee beans, here is a refund. Please order again!")
    else:
        print("your espresso was made")
        bank += MENU['espresso']['cost']
        resources['water'] -= MENU['espresso']['ingredients']['water']
        resources['coffee'] -= MENU['espresso']['ingredients']['coffee']
        print(f"Here is your change: ${round(change, 2)}")

#this is the cappuccino calculations for orders
def cappuccino():
    global bank  # have to modify global variable.
    global change
    # check if there are enough resources and subracts from total resources.
    if order < MENU['cappuccino']['cost']:
        print(f"you paid {order}, the cost of an cappuccino is {MENU['cappuccino']['cost']}\n"
              f"please order again.")
    elif resources['water'] < MENU['cappuccino']['ingredients']['water']:
        print("we are out of water, here is a refund. Please order again.")
    elif resources['coffee'] < MENU['cappuccino']['ingredients']['coffee']:
        print("we are out of coffee beans, here is a refund. Please order again!")
    elif resources['milk'] < MENU['cappuccino']['ingredients']['milk']:
        print("we are out of milk, here is a refund. Please order again.")
    else:
        print("your cappuccino was made")
        bank += MENU['cappuccino']['cost']
        resources['water'] -= MENU['cappuccino']['ingredients']['water']
        resources['coffee'] -= MENU['cappuccino']['ingredients']['coffee']
        print(f"Here is your change: ${round(change, 2)}")


#project begin
while cont:
    userI = input("what would you like to order (espresso/latte/cappuccino) ").lower()

    if userI == "report":
        print(f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml"
              f"\nCoffee: {resources['coffee']}g \nMoney: ${bank}")
    else:
        pay() #prompts user to input coins
        for i in range(len(payment)):
            order += payment[i]
            change = order - MENU[userI]['cost']
        if userI == "espresso":
            espresso()
        elif userI == "latte":
            latte()
        elif userI == "cappuccino":
            cappuccino()
        #used to repeat and clear all money values other than bank.
        userI = input("would you like another coffee? ").lower()

        if userI == "y" or userI == "yes":
            change = 0.0
            order = 0.0
            payment= []
            userI = ""
            cont = True
        else:
            print("thank you for your order, have a wonderful day!")
            cont = False



