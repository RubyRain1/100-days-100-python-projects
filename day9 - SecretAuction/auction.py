print(''' this will be ascii art soon ''')
print("Welcome to the secret auction program.")


 
cont = True

while cont:
#this is the start input 
    name = input("what is your name?: ")
    bid = input("what is your bid?: ")
    
    auctionL = [{"name": name, "bid": bid,}]
    

    #function to add nested dictionaries into a list to distinguish between auctioneers. 
    
    def auction(name, bid):
        auctiondict = {
            "name": name,
            "bid": bid
            }
        auctionL.append(auctiondict);
    userI = input("are there any other bidders? 'yes' or 'no'. ").lower()

    if userI == 'yes':
        cont = True
        
    elif userI == 'no':
        cont = False
        
auction(name, bid)
print(auctionL)