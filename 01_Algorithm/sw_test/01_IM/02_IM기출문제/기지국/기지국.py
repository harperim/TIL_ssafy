import sys
sys.stdin = open('기지국_input.txt')

T = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]


    # H인 곳 1로 표시
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'H':
                visited[i][j] = 1

    # 기지국 위치 기준 H인 곳 0으로 바꾸기
    for i in range(N):
        for j in range(N):
            # 길이 설정하기
            if arr[i][j] == 'A':
                M = 1
            elif arr[i][j] == 'B':
                M = 2
            elif arr[i][j] == 'C':
                M = 3
            else:
                continue
            for k in range(4):
                for l in range(1, M+1):
                    nx = i + dx[k] * l
                    ny = j + dy[k] * l
                    if 0 <= nx < N and 0 <= ny < N:
                        if arr[nx][ny] == 'H':
                            visited[nx][ny] = 0

    # 남은 H 개수 count
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 1:
                cnt += 1

    print(f'#{tc} {cnt}')
