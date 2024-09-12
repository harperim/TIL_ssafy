import sys
sys.stdin = open('최소비용_input.txt')

# def get_min():      # 힙 대용 O(N^2)
#     min_v = INF
#     for i in range(N):
#         for j in range(N):
#             if visited[i][j] == 0 and min_v > D[i][j]:
#                 min_v = D[i][j]
#                 x, y = i, j
#     return x, y
#
# def dijkstra(x, y):
#     # 출발점 설정
#     D[x][y] = 0
#     # 2차원 배열의 모든 요소를 선택
#     for _ in range(N*N):
#         # 방문하지 않은 요소 중에 가중치의 최소값 (heap 대용)
#         x, y = get_min()
#         # 방문체크
#         visited[x][y] = 1
#         # 인접정점의 가중치 업데이트
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             # 인덱스 체크, 방문체크, 벽체크
#             if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
#                 diff = 0        # 높이 차이
#                 if arr[nx][ny] > arr[x][y]:  # 오르막일 때만 diff를 계산
#                     diff = arr[nx][ny] - arr[x][y]
#                 # 가중치 갱신
#                 if D[nx][ny] > D[x][y] + 1 + diff:
#                     D[nx][ny] = D[x][y] + 1 + diff
#
# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     INF = int(1e9)
#     D = [[INF] * N for _ in range(N)]
#     visited = [[0] * N for _ in range(N)]
#
#     dijkstra(0, 0)
#     print(f'#{tc} {D[N-1][N-1]}')

# ---------------
# 2
import heapq


def dijkstra(x, y):
    # 출발점 설정
    heap = []
    D[x][y] = 0
    heapq.heappush(heap, (D[x][y], x, y))  # 가중치,  x, y

    while heap:  # 중복되어 갱신될 수 있으므로, N * N보다 커질 수 있음.
        d, x, y = heapq.heappop(heap)
        # 방문체크 :
        if visited[x][y]: continue
        visited[x][y] = 1

        if x == N - 1 and y == N - 1:  # 도착지점에 도착
            return

        # 인접정점 갱신
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 인접하고 방문 안한 정점
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                diff = 0
                if arr[nx][ny] > arr[x][y]:  # 오르막일때
                    diff = arr[nx][ny] - arr[x][y]
                if D[nx][ny] > D[x][y] + 1 + diff:  # 갱신
                    D[nx][ny] = D[x][y] + 1 + diff
                    heapq.heappush(heap, (D[nx][ny], nx, ny))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
INF = 987654321
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    D = [[INF] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    dijkstra(0, 0)
    print(f'#{tc} {D[N - 1][N - 1]}')


