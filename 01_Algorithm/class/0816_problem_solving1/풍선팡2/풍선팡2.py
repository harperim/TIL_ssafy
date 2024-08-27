import sys
sys.stdin = open('풍선팡2_input.txt')

T = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0

    for i in range(N):
        for j in range(M):
            sum_v = arr[i][j]
            # sum_v += arr[i][j]
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < N and 0 <= ny < M:
                    sum_v += arr[nx][ny]
            if max_v < sum_v:
                max_v = sum_v
    print(f'#{tc} {max_v}')





