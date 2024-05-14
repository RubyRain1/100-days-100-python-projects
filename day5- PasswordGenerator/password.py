import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nrletters= int(input("How many letters would you like in your password?\n")) 
nrsymbols = int(input(f"How many symbols would you like?\n"))
nrnumbers = int(input(f"How many numbers would you like?\n"))

    
total = int(nrletters) + int(nrnumbers) + int(nrsymbols)

#this is going to be a list that is appended based on what they add
password = [] * total


#this is the logic to append    

for i in range(0, nrsymbols):
    #this is to get a random character
    rand3 = random.randint(0, len(symbols))
    print(symbols[rand3], end="")
    
for i in range(0,nrletters):

    #this is to get a random character
    rand1 = random.randint(0,len(letters))
    print(letters[rand1], end="")

for i in range(0, nrnumbers):
    #this is to get a random character  
    rand2 = random.randint(0, len(numbers))
    print(numbers[rand2], end="")


