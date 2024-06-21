

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



def calculation():

    cont = True
    n1 = float(input("what is the first number? "))
    for key in mathC: #loop through dictionary to print operations
        print(key)


    while cont: #loop to get allow unlimted inputs.

        operationS = input("which operation do you want to use? ")
        n2 = float(input("what is the next number? "))

        operation = mathC
        firstanswer = operation(n1,n2)
        print(f"{n1} {operationS} {n2} = {firstanswer}")

        userI = input(f"Type 'y' to continue calculating with {firstanswer} or type 'new' to start a new calculation" +
        " or type 'n' to exit: ").lower()
        
        if userI == "y":
            n1 = firstanswer
        elif userI == "new":
            calculation()
        else:
            cont = False
calculation()


