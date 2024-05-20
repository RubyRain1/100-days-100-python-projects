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


for i in range(0,len(chosenword)):
    
    chosenlist.append("_")

while check in chosenlist:
   
    guess = input("guess a letter: ").lower()


    #checks if a letter is in the chosen word and then
    #sets it equal to the index in chosen list. 
    for i in range(0,len(chosenword)):
        if guess in chosenword[i]:
            chosenlist[i] = guess


    result = ' '.join(chosenlist)
    print(result)
