import art
import random
from gameInfo import data

#global variables 
score = 0
correct = True

def optionA():
    choiceA = random.randint(0,49)
    return choiceA

def optionB():
    choiceB = random.randint(0,49)
    return choiceB

#logo
print(art.logo)
while correct:
    choiceA = data[optionA()]
    choiceB = data[optionB()]

    #prevent pulling same dictionary
    if choiceA == choiceB:
        choiceA = data[optionA()]
        choiceB = data[optionB()]

    # #option a
    print(f"Compare A: {choiceA['name']}, {choiceA['description']}, from {choiceA['country']}")
    

    print(art.vs)

    # #option b   
    print(f"Against B: {choiceB['name']}, {choiceB['description']}, from {choiceB['country']}")
    


    userI = input("which option has the higher follower count: 'A' or 'B' ").lower()

    if choiceA['follower_count'] > choiceB['follower_count'] and userI == "a":
        print("\nyou win \n")
        score += 1
    elif choiceA['follower_count'] < choiceB['follower_count'] and userI == "a":
        print(art.logo)
        print("\nyou lose")
        print(f"your finals score is: {score}")
        correct = False
    elif choiceA['follower_count'] < choiceB['follower_count'] and userI == "b":
        print("\nyou win \n")
        score += 1
    else:
        print(art.logo)
        print("\nyou lose")
        print(score)
        correct = False