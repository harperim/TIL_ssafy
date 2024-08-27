import sys
sys.stdin = open('미로_input.txt')

def find_start(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return i, j


def dfs(x, y):
    global flag     # flag 달아주기
    visited[x][y] = 1
    if arr[x][y] == 3:
        flag = 1
        return      # 이전 단계로 리턴, 처음으로 리턴하지 않음

    # 네 방향 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 인덱스, 방문, 벽 체크
        if 0 <= nx < N and 0 <= ny < N and \
                visited[nx][ny] == 0 and \
            arr[nx][ny] != 1:
            dfs(nx, ny)


# 네 방향 탐색 전역에 작성, 한 번만 사용하면 되기 때문
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


T = int(input())

# 0 통로, 1 벽, 2 출발, 3 도착
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]  # 문자열 인덱싱 되기 때문에 붙어있는 경우 split 안 써도 됨
    visited = [[0] * N for _ in range(N)]

    sr, sc = find_start(arr)
    flag = 0  # 못 찾았다고 설정
    dfs(sr, sc)
    print(f'#{tc} {flag}')      # 아래 부분 먼저 써놓기 / top-down 방식  : 큰 것부터 보기

    # 재귀 : top-down => 큰 것부터 보고 세세한걸 나중에
    # DP : bottom-up
