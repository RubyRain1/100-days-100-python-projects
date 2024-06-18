

# + - / *
def add(n1,n2):
    return n1 + n2 

def subract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2 

def divide(n1,n2):
    return n1 / n2

mathC = {
    "+": add,
    "-": subract,
    "*": multiply,
    "/": divide
}

cont = True
n3 = 0

n1 = int(input("what is the first number? "))
  


for key in mathC: #loop through dictionary to print operations
    print(key)
operationS = input("which operation do you want to use? ")
n2 = int(input("what is the next number? "))

operation = mathC[operationS]
firstanswer = operation(n1,n2)
print(f"{n1} {operationS} {n2} = {firstanswer}")

while cont: #loop to get allow unlimted inputs.
    newanswer = operation(firstanswer, n3)

    userI = input(f"Type 'y' to continue calculating with {newanswer} or type 'n to exit").lower()
    if userI == 'y':
        for key in mathC: #loop through dictionary to print operations
            print(key)
        operationS = input("pick an operation: ")
        n3 = int(input("What is the next number? "))
        sum = newanswer
        newanswer = operation(newanswer, n3)
        print(f"{sum} {operationS} {n3} = {newanswer}")
        
    else: 
        print(f"thank you for using the calculator app!")
        cont = False
    

