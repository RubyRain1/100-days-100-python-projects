import random

cards =  [11,2,3,4,5,6,7,8,9,10,10,10,10]
phand = []
dhand = []
cont = True
#starting hand
def start():
    for i in range(2):
        rand = random.randint(0,12)
        rand2 = random.randint(0,12)
        phand.append(cards[rand])
        dhand.append(cards[rand2])
    shand1 = print(f"your starting hand is {phand}") #this is for the players starting hand
    shand2 = print(f"dealers starting hand is {dhand}") #this is for the dealers starting hand
    return shand1, shand2

start() #this begins the program by giving the player and dealer two values from the cards list.

while cont: #this will be the rest of the game
    phand.append(1)
    print(phand)
    cont = False




