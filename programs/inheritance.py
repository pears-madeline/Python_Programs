class A:
    def age(self):
        print("Age is 15")


class B:
    def age(self):
        print("Age is 22")

class C(A, B):
    def age(self):
        super(C, self).age()


c = C()
print(C.__mro__)
print(c.age())
#print(C.mro()) minimun resolution order

class Vehicle(object):

    #name = "vehicle"

    def __init__(self, name):
        self.name = name
        print(name, "Is a mini vehicle")

    def run(self):
        print(self.name,"vehicle can run ")

class Car(Vehicle):

    def __init__(self, name):
        print(name, "can carry 2 people")

        # Calling Parent class
        # Constructor
        super().__init__(name)

    def carry_passenger(self):
        print("carry passengers", self.name)

class ElectricCar(Car):

    def __init__(self, battery, name):
        self.battery = battery

        # Calling Parent class
        # Constructor
        super().__init__(name)

    def run_ev(self):
        print("ev ",self.name,self.battery)

ev = ElectricCar("500kv","Comet")
ev.run()
ev.run_ev()
ev.carry_passenger()


