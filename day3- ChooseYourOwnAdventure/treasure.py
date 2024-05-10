print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome To Treaure Island. \n Your mission is to find the treasure.")

#this will be taking user input 
userR = input("Would you like to begin the hunt? ")

#the game logi begins here.
if userR.lower() == "n":
    print("May you find your way home safely.. but beware the curse of the coward..")

elif userR.lower() == "y":
    userR = input("you come to a fork in the road you were traveling on, which direction will you choose? \n left or right? ")
    if userR.lower() == "right": #nested if because I want this if to be determined by the previous elif.
        print("You slip and fall breaking a bone, you are unable to continue.. GAME OVER")
    elif userR.lower() == "left":
        userR = input("You come to a beautiful lake, you can see the other side where your path continues. \n "+
              "You also spot a dock with an empty boat house. What do you do? \n Wait for a boat? Swim the distance? (swim or wait) ")
    if userR.lower() == "swim":
        print("You attempt to swim across the lake.. Unkown to you this lake is infested with hungry paranas! GAME OVER")
    elif userR.lower() == "wait":
        userR = input("You wait for a few minutes until a boat keeper pulls back up to the dock offering you a ride. \n "+
              "He takes you to the other side of the lake where you find three caves all glowing different colors. \n "+
              "The first glows an evil red, the second glows a searing yellow, the third glows a soothing blue.. \n "+
              "Which do you choose? (red, blue, yellow) ")
    if userR.lower == "blue":
        print("you are drawn in by the soothness of the blue.. reminding you of the waves hitting the beach.. the beautiful sky on a bright day.. \n "+ 
              "It's almost as if someone is singing to you.. As you enter the cave you see the hungry sirens singing their aluring song to you.. \n "+
              "GAME OVER")
    elif userR.lower() == "red":
        print("you are drawn to the evil red color.. Hoping that despite the fear enducing atmosphere that the treasure would lie within.. \n "+
              "Sadly you were mistaken, a trap triggers and that was it... GAME OVER")
    else:
        print("you decide to brave the yellow, despite it looking hot it is actually comforting as a warm embrace wraps \n "+
              "around you and guides you to the end of the cave where the treasure lies.. YOU WIN!!!")

