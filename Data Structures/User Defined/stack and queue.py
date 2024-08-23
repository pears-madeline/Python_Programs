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

#QUEUE

queue = []
queue.append('hii')
queue.append('hello')
queue.append('hey')
print("Initial queue")
print(queue)

print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print("\nQueue after removing elements")
print(queue)


