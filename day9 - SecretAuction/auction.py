from art import logo

print(logo)
print(''' this will be ascii art soon ''')
print("Welcome to the secret auction program.")


bids = {}

cont = True


#function to store highest bid FOR LOOP
def hBid(records): # creates new dictionary known as records
    highestbid = 0  
    winner = ""
    
    for key in records: #loops through the records dictionary to assign highest value and winner
        bidA = records[key]
        if bidA > highestbid:
            highestbid = bidA
            winner =  key
    print(f"winner is {winner} with amount of {highestbid}")
    
# #repeat auction WHILE LOOP
while cont:
    name = input("what is your name?: ")
    bid = int(input("what is your bid?: $"))
    bids[name] = bid
    userI = input("Would you like to place another bet?: ").lower()

    if userI == 'n' or userI == 'no':
        cont = False
        hBid(bids)
    else:
        cont = True
       


