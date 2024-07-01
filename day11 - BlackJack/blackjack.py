import random

cards =  [11,2,3,4,5,6,7,8,9,10,10,10,10]
phand = [] #players hand 
dhand = [] #dealers hand
cont = True #set as true for the while loop
userI = "" #this will be used for most user input.
pTotal = 0 #this allows for reference of player total
dTotal = 0 #this allows for reference of dealer total
cont2 = True
restart = True
bust = False
restart = False
hit = ""
newgame = ""
#starting hand
def start():
    for i in range(2):
        rand = random.randint(0,12)
        rand2 = random.randint(0,12)
        phand.append(cards[rand])
        dhand.append(cards[rand2])
    shand2 = print(f"dealers starting hand is {dhand}") #this is for the dealers starting hand
    shand1 = print(f"your starting hand is {phand}") #this is for the players starting hand
    return shand1, shand2

while cont: #this will be the rest of the game
    if not restart:
        #this is the beginning of the game 
        begin = input("would you like to play a game of black jack? ")
        if begin == "y":
            start() #this begins the program by giving the player and dealer two values from the cards list. 
        elif begin == "n": 
            print("thank you for playing")
    elif restart: 
        start()
        restart = False
    while hit != "n":
        hit = input("would you like to draw another card? ")
        randHit = random.randint(0,12)
        randHitD = random.randint(0,12)
        if hit == "y":
            #additional deal total
            if dTotal <17:
                dhand.append(cards[randHitD])
            elif dTotal > 21:
                dBust = True #this flag will be used later to win or lose game based on dealer bust 
            phand.append(cards[randHit])
            print(f"dealers hand: {dhand}")
            print(f"your hand: {phand}")
            for i in range(len(dhand)):
                dTotal += dhand[i]
        #this is the logic to end the game.
        elif hit == "n":
            if dTotal == 0:
                for i in range(len(dhand)):
                    dTotal += dhand[i]
            for i in range(len(phand)):
                pTotal += phand[i]
            if pTotal > 21:
                pBust = True
            else:
                if pTotal > dTotal:
                    print(f"dealer total: {dTotal}")
                    print(f"Player Total: {pTotal}")
                    newgame = input("you have succefully defeated the dealer YOU WIN!!! Would you like to play again? ")   
                elif dTotal > pTotal: 
                    print(f"dealer total: {dTotal}")
                    print(f"Player Total: {pTotal}")
                    newgame = input("Dealer Has Higher Total! YOU LOSE! Would you like to play again? ") 
                elif dTotal == pTotal:
                    print(f"dealer total: {dTotal}")
                    print(f"Player Total: {pTotal}")
                    newgame = input("BOTH TOTALS EQUAL!! DRAW!! Would you like to play again? ")  
                elif pBust == False and dBust == True:
                    newgame = input("DEALER BUST!! PLAYER WINS!! Would you like to play again? ")
                elif pBust == True and dBust == False: 
                    newgame = input("Player Bust Dealer Wins. Would you like to play again? ")
                elif pBust == True and dBust == True:
                    newgame = input("both player and dealer bust! DRAW!! Would you like to play again? ")
          

    if newgame == "y":
        dhand = [] #this will clear each list on restart
        phand = []
        dTotal = 0
        pTotal = 0
        hit = ""
        restart = True
    elif newgame == "n":
        cont = False
            





    