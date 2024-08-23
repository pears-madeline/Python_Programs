age = 21
if age >= 18:
    if age <= 30:
        print ("you are eligible to vote and you are youth")
    else:
        print("you are eligible to vote but your not youth")

age = int(input("enter a number : "))
if age > 18:
    print("you are eligible to vote")
elif age == 18:
    print("you can try next year")
elif age < 18:
    print("you are not eligible to vote")
else:
    print("welcome")