import sys
sys.stdin = open('파스칼의삼각형_input.txt')

T = int(input())

# 왼쪽 위, 위
dx = [-1, -1]
dy = [-1, 0]


# n x n의 절반만 채우면 됨
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            sum_val = 0

            # 열이 0인 경우
            if j == 0:
                arr[i][0] = 1
            else:
                for k in range(2):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        sum_val += arr[nx][ny]
                        arr[i][j] = sum_val
    # print(arr)
    print(f'#{tc}')

    for a in arr:
        line = ''
        for i in range(N):
            if a[i] != 0:
                line += str(a[i]) + ' '
        print(line)
