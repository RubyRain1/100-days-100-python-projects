import random

#global variables
answer = random.randint(1,100)
lives = 0 
cont = True

#beginning of game 
print("welcome to the number guessing game")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")


def restraint():
    global playerGuess
   
    if playerGuess > 100:
       playerGuess = int(input("Number exceeds restraints guess again: "))
    elif playerGuess < 1:
        playerGuess = int(input("Number exceeds restraints guess again: "))

    if playerGuess > answer:
        print("Too High")    
    elif playerGuess < answer:
        print("Too Low")
       


#set number of attempts
if difficulty == "easy":
    lives = 10
elif difficulty == "hard":
    lives = 5

#repeat guess w/ while loop
while cont:
    #start guesses
    print(f"you have {lives} attempts remaining to guess the number.")
    playerGuess = int(input("make a guess: "))

    if playerGuess > answer:
        print("Too High")
        lives -= 1
    elif playerGuess < answer:
        print("Too Low")
        lives -= 1
    elif playerGuess == answer:
        print("YOU WIN!!")
        print("thank you for playing!")
        cont = False
    if lives == 0: 
        print(f"No attempts remaining! YOU LOSE!! The correct answer was{answer}.")
        cont = False

    #runs the restraint function to keep player between 1-100
    if playerGuess > 100 or playerGuess <1:
        restraint()
        

