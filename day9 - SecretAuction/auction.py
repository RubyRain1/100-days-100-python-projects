print(''' this will be ascii art soon ''')
print("Welcome to the secret auction program.")


bids = {}
cont = True

while cont:
#this is the start input 
    name = input("what is your name?: ")
    bid = input("what is your bid?: ")
    bids[name] = bid
        
    userI = input("are there any other bidders? 'yes' or 'no'. ").lower()

    if userI == 'yes':
        cont = True
        
    elif userI == 'no':
        cont = False
        

