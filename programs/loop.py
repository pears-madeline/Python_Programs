print(1)
for i in range(1, 101):
    print(i)

str = "welcome"
len = len(str)
print("len is",len)
for i in range (0, len):
    print(i)
    print("str",str [i])




str1 = "welcome"
reverse = ""
for i in range(len - 1, -1, -1):
    print("index", str[i])
    reverse += str[i]
    print("revere", reverse)

for i in str:
    print("foreach loop", i)

    print("welcome")
    for i in range(1, 101):
        print("welcome")

    print(1)
    for i in range(1, 101):
        print(i)

    # while loop
    sum = 0
    for i in range(1, 101):
        sum += i
        print("sum", sum)

    i = 1
    while (i < 101):
        print("welcome")
        i += 1

# break
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

# continue
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#nested loop
#full pyramid pattern
def full_pyramid(n):
    for i in range(1, n + 1):
        for j in range(n - i):
            print(" ", end="")

        for k in range(1, 2 * i):
            print("*", end="")
        print()
full_pyramid(5)

# half pyramid pattern
def half_pyramid(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("* ", end="")
        print("")
n = 5
half_pyramid(n)

