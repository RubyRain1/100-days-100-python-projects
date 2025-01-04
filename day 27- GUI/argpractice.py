def add(*args):
    sum = 0
    for n in args:
        sum += n
        #OR
        #added = sum(args)
    #print(args) # either works!
    return sum


print(add(12,1,2))


class Car:

    def __init__(self, **kwargs):
        self.wheels = kwargs.get("wheels")
        self.model = kwargs.get("model")


my_car = Car(model= "nissan", wheels="off road")

print(my_car.model)

