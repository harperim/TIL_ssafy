stack = []

stack.append(1)  # push(1)
stack.append(2)  # push(2)
stack.append(3)  # push(3)
print(stack.pop())
print(stack.pop())
print(stack.pop())

size = 10
stack = [0] * size
top = -1

# push
top += 1
stack[top] = 1

top += 1
stack[top] = 2

top += 1
stack[top] = 3

# pop
while top != -1:    # Not IsEmpty
    print("Stack is Empty")
    top -= 1





