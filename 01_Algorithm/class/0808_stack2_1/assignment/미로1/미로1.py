import sys
sys.stdin = open('미로1_input.txt')


def find_start(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return i, j


def dfs(x, y):
    global flag
    visited[x][y] = 1  # 방문체크
    if arr[x][y] == 3:
        flag = 1
        return

    # 시작정점에 인접한 정점(4방향) 중에서 방문 안한 정점 -> 재귀
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 인덱스, 방문, 벽 / 3가지 꼭 기억하기! 인/방/벽!!!
        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and \
                arr[nx][ny] == 0 or arr[nx][ny] == 3:
            dfs(nx, ny)


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
T = 10
N = 16
for tc in range(1, T + 1):
    no = input()  # dummy
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    flag = 0
    sx, sy = find_start(arr)
    dfs(sx, sy)
    print(f'#{tc} {flag}')
