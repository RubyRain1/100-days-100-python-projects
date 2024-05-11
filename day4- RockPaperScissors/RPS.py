import random 


#this is the cpu logic very simple
cpu = random.randint(0,2)

player = int(input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors "))

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

userchoice = [rock, paper, scissors]

#this is the rock logic
if player == 0 and cpu == 0:
    print(userchoice[0])
    print(f"computer chose: \n \n {userchoice[0]} \n You Draw")

if player == 0 and cpu == 1:
    print(userchoice[0])
    print(f"computer chose: \n \n {userchoice[1]} \n You Lose")

if player == 0 and cpu == 2:
    print(userchoice[0])
    print(f"computer chose: \n \n {userchoice[2]} \n You Win!!!")

#this is the paper logic
if player == 1 and cpu == 1:
    print(userchoice[1])
    print(f"computer chose: \n \n {userchoice[1]} \n You Draw")

if player == 1 and cpu == 0:
    print(userchoice[1])
    print(f"computer chose: \n \n {userchoice[0]} \n You Win!!!")

if player == 1 and cpu == 2:
    print(userchoice[1])
    print(f"computer chose: \n \n {userchoice[2]} \n You Lose")

#this is the scissors logic
if player == 2 and cpu == 2:
    print(userchoice[1])
    print(f"computer chose: \n \n {userchoice[2]} \n You Draw")

if player == 2 and cpu == 0:
    print(scissors)
    print(f"computer chose: \n \n {userchoice[0]} \n You Lose")

if player == 2 and cpu == 1:
    print(scissors)
    print(f"computer chose: \n \n {userchoice[1]} \n You Win")


    