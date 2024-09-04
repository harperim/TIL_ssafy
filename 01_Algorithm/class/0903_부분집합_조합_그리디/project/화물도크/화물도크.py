import sys
sys.stdin = open('화물도크_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort(key=lambda x: (x[1], x[0]))

    cnt = 0
    finish = 0
    for i in range(N):
        if finish <= arr[i][0]:
            cnt += 1
            finish = arr[i][1]
    print(f'#{tc} {cnt}')
