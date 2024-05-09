print("Welcome to the tip calculator!")

total = float(input("what was the total bill? $"))
perctip = float(input("how much tip would you like to give? 10, 12, or 15? "))
people = int(input("how many people to split the bill? "))

tip = round((total / people) * ((perctip/100)+1), 2)
tip = "{:.2f}".format(tip)
print(f"each person should pay: ${tip}") 