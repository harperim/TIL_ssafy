import sys
sys.stdin = open('회전_input.txt')

T = int(input())

# n = input().split()

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    Q_SIZE = N + 1
    cQ = [0] * Q_SIZE
    front = rear = 0

    # 큐 만들기
    for i in range(N):
        rear = (rear + 1) % Q_SIZE  # enq(1)
        cQ[rear] = arr[i]

    # print(cQ)

    # M번만큼 이동하기
    for i in range(M):
        move = cQ.pop(1)
        cQ.append(move)

    print(f'#{tc} {cQ[1]}')

# 강사님 풀이
for


