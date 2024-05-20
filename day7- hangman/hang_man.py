import random


#this file will hold key variables that are going to be used in solution.py
wList = ["ardvark", "baboon", "camel", "zebra"]
chosenlist = []
wrong = 0 
check = "_"

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


title = '''
  _                                             
 | |                                            
 | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
 | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | | | | (_| | | | | (_| | | | | | | (_| | | | |
 |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |                      
                    |___/                       
                    '''
#this will choose a random word based off index number
rnum = random.randint(0,3)

#assigns the random number in order to get the string instead of index number
chosenword = wList[rnum]

#this populates a list full of _'s to act as the blank template.
for i in range(0,len(chosenword)):
    
    chosenlist.append("_")



 