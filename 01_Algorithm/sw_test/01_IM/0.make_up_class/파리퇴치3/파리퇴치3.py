import sys
sys.stdin = open('파리퇴치3_input.txt')

T = int(input())

# 우하좌상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# cross (대각선 방향)
dci = [-1, 1, 1, -1]
dcj = [1, 1, -1, -1]

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_val = max_val1 = max_val2 = 0

    # 상하좌우 합의 최대값 구하기
    for i in range(N):
        for j in range(N):
            sum_val1 = arr[i][j]
            for l in range(1, M):
                for k in range(4):
                    ni = i + di[k]*l
                    nj = j + dj[k]*l
                    if 0 <= ni < N and 0 <= nj < N:
                        sum_val1 += arr[ni][nj]
                if max_val1 < sum_val1:
                    max_val1 = sum_val1

    # 대각선 합의 최대값 구하기
    for i in range(N):
        for j in range(N):
            sum_val2 = arr[i][j]
            for l in range(1, M):
                for k in range(4):
                    ni = i + dci[k]*l
                    nj = j + dcj[k]*l
                    if 0 <= ni < N and 0 <= nj < N:
                        sum_val2 += arr[ni][nj]
                if max_val2 < sum_val2:
                    max_val2 = sum_val2

    # 상하좌우, 대각선 합 중 더 큰 값 출력
    if max_val1 >= max_val2:
        max_val = max_val1
    else:
        max_val = max_val2

    print(f'#{tc} {max_val}')

