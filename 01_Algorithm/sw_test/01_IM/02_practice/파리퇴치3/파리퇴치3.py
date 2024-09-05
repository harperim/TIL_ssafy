import sys
sys.stdin = open('파리퇴치3_input.txt')

T = int(input())

# 해당 칸의 주변 8칸 모두 가져옴
dx_s = [0, 1, 0, -1]
dy_s = [1, 0, -1, 0]
dx_c = [1, 1, -1, -1]
dy_c = [1, -1, -1, 1]

for tc in range(1, T+1):
    N, M = map(int, input().split())  # 5 2
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0

    for i in range(N):
        for j in range(N):
            sum_v = 0
            sum_v += arr[i][j]

            for l in range(1, M+1):
                for k in range(4):
                    nx_s = i + dx_s[k]*l
                    ny = j + dy_s[k]*l


                    if 0 <= nx < N and 0 <= ny < N:
                        sum_v += arr[nx][ny]

            if max_v < sum_v:
                max_v = sum_v
    print(max_v)

