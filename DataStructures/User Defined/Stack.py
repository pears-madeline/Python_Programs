# FIRST IN FIRST OUT FIFO QUEUE append \ pop
# LAST IN FIRST OUT LIFO STACK append \ pop

#STACK

str = "hello everyone"

stack = []

for i in str:
    stack.append(i)

print(stack)

while stack:
    print(stack.pop())

s=str.split(" ")

print(s)




