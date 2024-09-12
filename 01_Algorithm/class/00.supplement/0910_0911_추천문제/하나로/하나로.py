import sys
sys.stdin = open('하나로_input.txt')

from heapq import heappush, heappop


def prim(s):
    # 출발점 셋팅
    total = 0  # 정답
    pq = []  #
    D[s] = 0
    heappush(pq, (D[s], s))  # 가중치, 섬번호
    while pq:
        # 방문하지 않고 가중치의 최소값
        d, v = heappop(pq)
        if visited[v]: continue

        # 방문체크
        visited[v] = 1
        total += d * tax

        # 인접한 정점중에 방문 안 한 정점을 갱신
        for w in range(N):  # 모든 정점이 연결된 완전그래프
            if visited[w] == 0 and D[w] > dist[v][w]:
                D[w] = dist[v][w]
                heappush(pq, (D[w], w))

    return total


T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 섬의 갯수
    x_arr = list(map(int, input().split()))  # X죄표들
    y_arr = list(map(int, input().split()))  # Y죄표들
    tax = float(input())  # 환경부담세율

    # 섬들간의 거리의 제곱
    dist = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(i + 1, N):  # 대각선방향의 윗쪽 반만 구함
            dist[i][j] = dist[j][i] = (x_arr[i] - x_arr[j]) ** 2 + (y_arr[i] - y_arr[j]) ** 2

    # prim 변수들
    INF = int(1e25)
    D = [INF] * N  # 가중치
    visited = [0] * N

    print(f'#{tc} {prim(0):.0f}')