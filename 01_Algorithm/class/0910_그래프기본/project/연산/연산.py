import sys
sys.stdin = open('연산_input.txt')

from collections import deque

def bfs(v):
    # Q = []  # 시간초과
    Q = deque()
    Q.append(v)
    visited[v] = 1
    while Q:
        # v = Q.pop(0)  # 시간초과
        v = Q.popleft()
        # 하고 싶은 일
        if v == M:
            return visited[v] - 1
        # 인접, 미방문
        for w in [v + 1, v - 1, v * 2, v - 10]:
            if 0 < w <= 1000000 and visited[w] == 0:
                Q.append(w)
                visited[w] = visited[v] + 1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    visited = [0] * 1_000_001
    print(f'#{tc} {bfs(N)}')


