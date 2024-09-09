import sys
sys.stdin = open('농작물수확하기_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    total = 0
    middle = N // 2
    for i in range(N):
        if i < middle:
            start = middle - i
        else:
            start = i - middle

        end = N - start
        for j in range(start, end):
            total += arr[i][j]

    print(f'#{tc} {total}')
