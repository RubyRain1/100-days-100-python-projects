import random

wList = ["ardvark", "baboon", "camel"]
chosenlist = []
wrong = 0 
check = "_"
#this will choose a random word based off index number
rnum = random.randint(0,2)

#assigns the random number in order to get the string instead of index number
chosenword = wList[rnum]
print(chosenword)

#this populates a list full of _'s to act as the blank template.
for i in range(0,len(chosenword)):
    
    chosenlist.append("_")



 