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
#this is the rock logic
if player == 0 and cpu == 0:
    print(rock)
    print(f"computer chose: \n \n {rock} \n You Draw")

if player == 0 and cpu == 1:
    print(rock)
    print(f"computer chose: \n \n {paper} \n You Lose")

if player == 0 and cpu == 2:
    print(rock)
    print(f"computer chose: \n \n {scissors} \n You Win!!!")

#this is the paper logic
if player == 1 and cpu == 1:
    print(paper)
    print(f"computer chose: \n \n {paper} \n You Draw")

if player == 1 and cpu == 0:
    print(paper)
    print(f"computer chose: \n \n {rock} \n You Win!!!")

if player == 1 and cpu == 2:
    print(paper)
    print(f"computer chose: \n \n {scissors} \n You Lose")

#this is the scissors logic
if player == 2 and cpu == 2:
    print(scissors)
    print(f"computer chose: \n \n {scissors} \n You Draw")

if player == 2 and cpu == 0:
    print(scissors)
    print(f"computer chose: \n \n {rock} \n You Lose")

if player == 2 and cpu == 1:
    print(scissors)
    print(f"computer chose: \n \n {rock} \n You Win")