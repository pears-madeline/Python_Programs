# '''
# Check if a number is divisible by 2,3,4
# If a number is divisible by 2, print “divide by 2”
# If a number is divisible by 3, print “divide by 3”
# If a number is divisible by 4, print “divide by 4”
# If the number is not divisible by 2,3,4 then print “Not divisible by 2,3,4”
# '''
number = int(input("enter a number : "))
if number //2 == 0 :
    print ("divisible by 2")
elif number //3 == 0 :
    print (" divisible by 3")
elif number //4 == 0 :
    print ("divisible by 4")
else:
    print ("not divisible by 2, 3, 4")

# '''
# Print Grade based on marks
# Mark > 90 - print O grade
# Mark > 80 - print A grade
# Mark > 70 - print B grade
# Mark > 60 - print C grade
# Mark > 50 - print D grade
# Mark < 50 - print fail
# '''

mark = int(input("enter a value : "))
if mark > 90 :
    print("O grade")
elif mark > 80:
    print ("A grade")
elif mark > 70:
    print("B grade")
elif mark > 60:
    print("C grade")
elif mark > 50:
    print("D grade")
else:
    print("fail")

# '''
#  Write a program to find the given number is odd or even
#  write the program about the fizzbuzz
#  if the number is divisible by 3 print(Fizz)
#  if the number is divisible by 5 print(buzz)
#  if the number is divisible by 3 and 5 print(Fizzbuzz)
# '''
number = int(input("enter a number : "))
if number %3 == 0 and number %5 == 0:
    print ("fizzbuzz")
elif number %3 == 0:
    print("fizz")
elif number %5 == 0:
    print("buzz")
else:
    print("hi")



