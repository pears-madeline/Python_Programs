#object oriented programming language oops
# 1. class its like a blueprint to create a object
# 2. object is a instance of class
# 3.concept
# inheritante, encapsulation, abstraction, polymorphism SUPER() DISplay details, types single  multi level multiple

#object has 2 things attribute and behaviour

class Vehicle:

    #attributes of class. Attributes are always public
    colour = "matte black"
    wheel = "4"
    name = "car"

    # Args Constructor
    def __init__(self, colour, wheel):
        print("args constrcutor called")
        self.colour = colour
        self.wheel = wheel

    def run(self):
        print("colour {} name {}".format(self.colour,self.wheel))

    def __eq__(self, other):
        if isinstance(other, Vehicle):
            if other.colour == self.colour and other.wheel == self.wheel:
                return True
        return False

    def __str__(self) -> str:
        return f"{self.colour}({self.wheel}) {self.name}"

vehicle = Vehicle("grey",3)

print("vehicle ",isinstance(vehicle,Vehicle))


#class variables
print(vehicle.__class__.colour)
print(vehicle.__class__.wheel)

#instance variables
print(vehicle.colour)
print(vehicle.wheel)
vehicle.run()

vehicle1 = Vehicle("black",4)
vehicle1.run()

print("vehicle == vehicle1 ",vehicle == vehicle1)

vehicle1.wheel = 3
vehicle1.colour = "red"

print("vehicle eq vehicle1 ",vehicle.__eq__(vehicle1))


vehicle.colour = "cian"
print("vehicle ",vehicle)
del vehicle.colour
print("vehicle ",vehicle)
del vehicle
#print("vehicle ",vehicle)









