import random

cards =  [11,2,3,4,5,6,7,8,9,10,10,10,10]
phand = [] #players hand 
dhand = [] #dealers hand
cont = True #set as true for the while loop
userI = "" #this will be used for most user input.
pTotal = 0 #this allows for reference of player total
dTotal = 0 #this allows for reference of dealer total
cont2 = True
bust = False
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
    
def dealer(dTotal, cont2, bust):
    
    while cont2:
        randHit = random.randint(0,12) #this will be used for the player and dealer hitting.
        if dTotal < 17:
            dhand.append(cards[randHit])
            for i in range(len(dhand)):
                dTotal += dhand[i - 1]
        elif dTotal > 17:
             cont2 = False
    if dTotal > 21:
        print(f"dealer bust with {dTotal}")
        bust = True
    else: 
        print(f"dealers total: {dTotal}")
    print(dhand)   
    return bust
def player(pTotal, cont2, dhand):   
    hit = input("would you like to draw another card? ")
    while cont2:
        randHit = random.randint(0,12) #this will be used for the player and dealer hitting.
        if hit == "y":
            phand.append(cards[randHit])
            print(f"dealers hand: {dhand}")
            print(f"players hand: {phand}")
            hit = input("would you like to draw another card? ")
        else:
            for i in range(len(phand)):
                pTotal += phand[i]
                cont2 = False
    if dealer(dTotal, cont2, bust) == True:
        print("the dealer busted")
    else: 
        print("this works")
    return print(pTotal)
#this is the beginning of the game 
begin = input("would you like to play a game of black jack? ")
if begin == "y":
    start() #this begins the program by giving the player and dealer two values from the cards list. 
elif begin == "n": 
    print("thank you for playing")

while cont: #this will be the rest of the
    dealer(dTotal, cont2, bust)
    player(pTotal, cont2, dhand)
    
    cont = False



