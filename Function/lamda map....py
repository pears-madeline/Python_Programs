numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

print("Original list of integers:")
print(numbers)
print("Even numbers from the said list:")
print(even_numbers)
print("Odd numbers from the said list:")
print(odd_numbers)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_numbers = list(map(lambda x: x ** 2, numbers))
cubed_numbers = list(map(lambda x: x ** 3, numbers))

print("Original list of integers:")
print(numbers)
print("Squared numbers from the said list:")
print(squared_numbers)
print("Cubed numbers from the said list:")
print(cubed_numbers)


starts_with = lambda string, char: string.startswith(char)
string = "Hello"
char = "H"

if starts_with(string, char):
    print(f"The string '{string}' starts with the character '{char}'.")
else:
    print(f"The string '{string}' does not start with the character '{char}'.")


from datetime import datetime
current_datetime = datetime.now()

extract_year = lambda dt: dt.year
extract_month = lambda dt: dt.month
extract_day = lambda dt: dt.day
extract_time = lambda dt: dt.time()

year = extract_year(current_datetime)
month = extract_month(current_datetime)
day = extract_day(current_datetime)
time = extract_time(current_datetime)

print("Current datetime:", current_datetime)
print("Year:", year)
print("Month:", month)
print("Day:", day)
print("Time:", time)


is_number = lambda s: s.replace('.', '', 1).isdigit() if s else False

string1 = "123.45"
string2 = "abc123"
string3 = ""

print(f"Is '{string1}' a number? {is_number(string1)}")
print(f"Is '{string2}' a number? {is_number(string2)}")
print(f"Is '{string3}' a number? {is_number(string3)}")


