# 다익스트라 + 인접행렬
'''
서울(0), 천안(1), 원주(2), 논산(3), 대전(4),
대구(5), 강릉(6), 광주(7), 부산(8), 포항(9)
'''
'''
9 14
0 1 12
0 2 15
1 3 4
1 4 10
2 5 7
2 6 21
3 4 3
3 7 13
4 5 10
5 8 9
5 9 19
6 9 25
7 8 15
8 9 5
'''
import heapq

def prim(v):
    total = 0
    heap = []
    # 출발점의 가중치 셋팅(0), 힙에 enQ
    D[v] = 0
    heapq.heappush(heap,(D[v], v))

    while heap:
        # 방문하지 않고, 가중치가 최소값이 정점 찾기
        dist, v = heapq.heappop(heap)
        if visited[v]: continue
        visited[v] = 1
        total += dist       # 비용 계산
        # 선택한 노드에 인접한 정점의 가중치 업데이트
        for w in range(1, V+1):
            if adj_mat[v][w]  and not visited[w]:
                if D[w] >  adj_mat[v][w]:
                    D[w] = adj_mat[v][w]
                    heapq.heappush(heap, (D[w], w))

    return total

V, E = map(int, input().split())
adj_mat = [[0] * (V+1) for _ in range(V+1)]  # 인접행렬
INF = int(1e9)          # 1.0 X 10 ^ 9
D = [INF] * (V+1)       # 가중치
visited = [0] * (V+1)

for i in range(E):
    s, e, d = map(int, input().split())
    adj_mat[s][e] = d
    adj_mat[e][s] = d

print(prim(0))             # 서울(0)
print(D)


# prim은 보통 비용을 추가 => total 추가
# D[v] + : 부분 지우기
