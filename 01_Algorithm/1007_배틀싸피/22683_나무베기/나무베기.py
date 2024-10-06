import sys
sys.stdin = open('나무베기_input.txt')

from collections import deque

# 방향 벡터: 상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(startx, starty, goalx, goaly, N, K, grid):
    # 방문 기록 배열 초기화
    visited = [[[[False for _ in range(K + 1)] for _ in range(4)] for _ in range(N)] for _ in range(N)]
    q = deque([(startx, starty, 0, 0, 0)])  # (x, y, 방향, 이동 횟수, 컷 수)
    visited[startx][starty][0][0] = True  # 시작 위치 방문 처리

    while q:
        curx, cury, dir, count, cut = q.popleft()

        # 목표 도달 확인
        if curx == goalx and cury == goaly:
            return count

        # 오른쪽으로 회전
        if not visited[curx][cury][(dir + 1) % 4][cut]:
            visited[curx][cury][(dir + 1) % 4][cut] = True
            q.append((curx, cury, (dir + 1) % 4, count + 1, cut))

        # 왼쪽으로 회전
        if not visited[curx][cury][(dir + 3) % 4][cut]:
            visited[curx][cury][(dir + 3) % 4][cut] = True
            q.append((curx, cury, (dir + 3) % 4, count + 1, cut))

        # 현재 방향으로 전진
        ni = curx + dx[dir]
        nj = cury + dy[dir]

        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj][dir][cut]:
            if grid[ni][nj] == 'T':
                if cut < K:
                    visited[ni][nj][dir][cut + 1] = True
                    q.append((ni, nj, dir, count + 1, cut + 1))
            else:
                visited[ni][nj][dir][cut] = True
                q.append((ni, nj, dir, count + 1, cut))

    return -1  # 목표에 도달할 수 없는 경우


def main():
    T = int(input())  # 테스트 케이스 수 입력
    for tc in range(1, T + 1):
        N, K = map(int, input().split())  # 맵의 크기(N)와 최대 컷 수(K)
        grid = []
        for i in range(N):
            s = input().strip()
            grid.append(list(s))  # 각 줄을 리스트로 변환하여 2차원 배열 생성
            if 'X' in s:
                startx, starty = i, s.index('X')  # 시작점
            if 'Y' in s:
                goalx, goaly = i, s.index('Y')  # 목표점

        result = bfs(startx, starty, goalx, goaly, N, K, grid)
        print(f"#{tc} {result}")


if __name__ == "__main__":
    main()