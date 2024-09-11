'''
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

from heapq import heappush, heappop

def prim(start):
    heap = list()
    MST = [0] * (V)

    # 최소 비용 합계
    sum_weight = 0

    # 힙에서 관리해야 할 데이터
    # 가중치, 정점 정보
    # heappush(heap, (start, 0))  # 정점 번호를 기준으로 정렬이 되기 때문에 안 됨
    heappush(heap, (0, start))  # 시작점은 가중치가 0이다.

    while heap:
        weight, v = heappop(heap)  # 현재 시점에서 가중치가 가장 작은 정점이 pop
        
        # 이미 방문한 지점이면 통과
        if MST[v]:
            continue

        # 방문 처리
        MST[v] = 1
        # 누적합 추가
        sum_weight += weight  # BFS + 그리디(최소 비용 정점을 먼저 선택)

        # 갈수 있는 노드를 보면서
        for next in range(V):
            # 갈 수 없는 지점이면 continue
            if graph[v][next] == 0:
                continue

            # 이미 방문한 지점이면 continue
            if MST[next]:
                continue

            heappush(heap, (graph[v][next], next))

    return sum_weight


V, E = map(int, input().split())
# 인접리스트가 더 좋은데 왜 인접행렬로 사용?
# => [선택과제] 인접 리스트로 변경
# A : [(32, B)] : 가중치만큼 B로 갈 수 있다는 뜻 / list, tuple, class 구조로 사용
graph = [[0] * (V) for _ in range(V)]  # 인접 행렬로 구현

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u][v] = w
    graph[v][u] = w  # 가중치가 있는 무방향 그래프

result = prim(0)
print(f'최소 비용 = {result}')  # 최소 비용 = 175
