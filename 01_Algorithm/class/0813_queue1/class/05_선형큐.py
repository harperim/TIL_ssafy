SIZE = 100
Q = [0] * SIZE
front = rear = -1

# enQ
rear += 1
Q[rear] = 1

# deQ
while front != rear:
    front += 1
    print(Q[front])
