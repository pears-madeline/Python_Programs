#1. Write a Python program that defines a method to calculate the area of a rectangle.
def area_of_rectangle(width, height):
    return width * height
width = 4
height = 8
print ("area of rectangle:",area_of_rectangle(width, height))

#2. Create a method that accepts a list of integers and returns the sum of all the elements in the array.
def sum_of_list(numbers):
    return sum(numbers)
numbers = [1, 2, 3, 4, 5, 6, 7]
print("Sum of List:", sum_of_list(numbers))

#3. Implement method overloading for a "print" method that can print different types of data such as int, double, and String.
def print_data(data):

    if isinstance(data, int):
        print(f"Integer: {data}")
    elif isinstance(data, float):
        print(f"Double: {data}")
    elif isinstance(data, str):
        print(f"String: {data}")
    else:
        print("Unsupported type")

print_data(55)
print_data(3.17)
print_data("Hello, People!")
print_data([1, 2, 3])

#4. Print a multiplication table for a given number.
def multiplication_table(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")
multiplication_table(10)

#5. Write a program to Count how many digits in a number.
def count_digits(number):
    return len(str(abs(number)))
number = 98761234
print("Count of Digits:", count_digits(number))

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
number = 29
print(f"Is {number} a prime number? {is_prime(number)}")

#6. Write a program to Check if a number is prime
def primes_up_to(limit):
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

#7.  Write a program to Find all prime numbers up to a given number.
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
limit = 80
print(f"Prime numbers up to {limit}: {primes_up_to(limit)}")

#8.  Write a program to Print a factorial of a number.
def factorial(number):
    if number < 0:
        return "Undefined for negative numbers"
    elif number == 0:
        return 1
    else:
        fact = 1
        for i in range(1, number + 1):
            fact *= i
        return fact
number = 5
print(f"Factorial of {number}: {factorial(number)}")

#9.  Write a program to Print fibonacci series.
def fibonacci_series(n):
    a, b = 0, 1
    series = []
    while len(series) < n:
        series.append(a)
        a, b = b, a + b
    return series
terms = 10
print(f"Fibonacci series with {terms} terms: {fibonacci_series(terms)}")

#
def perform_operation():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (add / subtract / multiply / divide): ").strip().lower()

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 != 0:
                result = num1 / num2
            else:
                return "Error: Division by zero is not allowed."
        else:
            return "Invalid operation. Please enter add, subtract, multiply, or divide."

        return f"The result of {operation} is: {result}"

    except ValueError:
        return "Invalid input. Please enter numeric values for numbers."

def perform_operation():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (add / subtract / multiply / divide): ").strip().lower()

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 != 0:
                result = num1 / num2
            else:
                return "Error: Division by zero is not allowed."
        else:
            return "Invalid operation. Please enter add, subtract, multiply, or divide."

        return f"The result of {operation} is: {result}"

    except ValueError:
        return "Invalid input. Please enter numeric values for numbers."
print(perform_operation())

#map
#lambda


