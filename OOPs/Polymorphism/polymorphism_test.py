# 2 types compile time, run time
#compile time-overloading-1. constructor 2. function 3. operator
# run time - overriding
#cpompile timeee
from multipledispatch import dispatch

class Employee:
    __bonus = 0
    # private member
    __salary = 0
    # constructor
    @dispatch(str)
    def __init__(self, name):
        # public data member
        print("1 arg constructor")
        self.__name = name

    @dispatch(str,int)
    def __init__(self, name, salary):

        print("2 args constructor")
        # public data member
        self.__name = name

        # private member
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    @dispatch(float)
    def add_salary(self, bonus):
        print("arg 1 salary")
        self.__salary += bonus

    @dispatch(float, float)
    def add_salary(self, bonus, incentives):
        print("arg 1 salary")
        self.__salary += bonus + incentives

    def set_salary(self, newsal):
         self.__salary = newsal

    def __str__(self) -> str:
        return f"{self.__name}({self.__salary} {self.__bonus})"

# creating object of a class
emp = Employee('AAA')

emp.salary = 3000000000
emp.set_salary(100)
print(emp.get_salary())

emp1 = Employee('James', 100000)
print(emp1.get_salary())
emp1.name = "hello"
print(emp1)

emp1.add_salary(15000.01)
print(emp1.get_salary())

emp2 = Employee('Roshan', 200000)
emp2.add_salary(20000.01,10000.50)
print(emp2.get_salary())

#runtimee

class Animal:
    def make_sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def make_sound(self):
        print("Dog barks")

my_animal = Dog()
my_animal.make_sound()  # Calls the overridden method in the Dog class
my_animal = Animal()
my_animal.make_sound()

#duck typing
class Bird:
    def fly(self):
        pass

class Sparrow(Bird):
    def fly(self):
        print("Sparrow flies")

class Airplane:
    def fly(self):
        print("Airplane flies")

def perform_flight(obj):
    obj.fly()

sparrow = Sparrow()
airplane = Airplane()

perform_flight(sparrow)  # Output: Sparrow flies
perform_flight(airplane)  # Output: Airplane flies


# parametric polymorphism
from typing import TypeVar

T = TypeVar('T')

def print_item(item: T):
    print(item)

print_item(42)         # Works with integers
print_item("Hello")    # Works with strings
