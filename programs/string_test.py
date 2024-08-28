str = "Hello World Welcome"
#---> indexing
print("string is ",str)
print("index 0 is ",str[0])
print("index 4 is ",str[4])
print("index 5 is ",str[5])
print(str[10])
print("last value ",str[-3])
print(str[-6])

#---> slicing
str1 = str[: 3]
print("str1 ",str1)
print("slice ",str[2: 3])

str2 = str[1 : 5 : 2]
print("str 2", str2)
print("slice 2 ", str[0 : 5 : 2])

str3 = str[-1 : -12 : -2]
print("reverse slice 1", str3)
print("reverse slice 2",str[-1 : -12 : -2])

str5 = "HeLLo"
print("upper ",str5.upper())
print("lower ",str5.lower())
print("swapcase ",str5.swapcase())

b = "Hello, World!"
print(b[2:])

#---> modify stringssx
# upper case
a = "Hello, World!"
print(a.upper())

# lower case
a = "Hello, World!"
print(a.lower())

# remove white space
a = " Hello, World! "
print(a.strip())

#---> concatenate strings
a = "Hello"
b = "World"
c = a + b
print(c)

# to add space
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#---> format strings

# f string
age = 36
txt = f"My name is John, I am {age}"
print(txt)

# placeholders and modifiers
price = 59
txt = f"The price is {price} dollars"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

#---> escape characters
txt = "We are the so-called \"Gang A\" from our school."
print(txt)

#---> string methods

txt = "hii, and welcome to my city."
x = txt.capitalize()
print (x)

txt = "Hii, And Welcome To My City!"
x = txt.casefold()
print (x)

txt = "blueberry"
x = txt.center(20)
print(x)

txt = "I love lychee, lychee are my favorite fruit"
x = txt.count("lychee")
print(x)

txt = "My name is peårs"
x = txt.encode()
print(x)

txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)

txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x)

txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)

txt = "Company12"
x = txt.isalnum()
print(x)

txt = "CompanyX"
x = txt.isalpha()
print(x)

txt = "Company123"
x = txt.isascii()
print(x)

txt = "1234"
x = txt.isdecimal()
print(x)

txt = "50800"
x = txt.isdigit()
print(x)

txt = "Demo"
x = txt.isidentifier()
print(x)

txt = "hello world!"
x = txt.islower()
print(x)

txt = "565543"
x = txt.isnumeric()
print(x)

txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x)

txt = "   "
x = txt.isspace()
print(x)

txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x)

myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")

txt = "Hello my FRIENDS"
x = txt.lower()
print(x)

txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")

txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))

txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)

txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)

txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)

txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(x)

txt = "banana"
x = txt.rjust(20)
print(x, "is my favorite fruit.")

txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)

txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x)

txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")

txt = "welcome to the jungle"
x = txt.split()
print(x)

txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)

txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)

txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")

txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)

txt = "Welcome to my world"
x = txt.title()
print(x)

#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))

txt = "Hello my friends"
x = txt.upper()
print(x)

txt = "50"
x = txt.zfill(10)
print(x)

# '''
# Reverse the words in the given string program using
# Loop
# Stack
# Reverse method
# slicing
# Python program to print even length words in a string
# Python program to check if a string has at least one letter and one number
# Remove All Duplicates from a Given String in Python
# '''
