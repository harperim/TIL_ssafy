'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''


def bfs(v):
    # enQ + 방문체크
    Q = []
    Q.append(v)  # -> Q = [v]
    visited[v] = 1

    while Q:
        v = Q.pop(0)     # v = deQ
        # 시작정점(v)의 인접하고 방문 안 한 정점(w)
        for w in adj_list[v]:
            if visited[w] == 0:
                # enQ + 방문체크
                Q.append(w)
                visited[w] = visited[v] + 1


V, E = map(int, input().split())
temp = list(map(int, input().split()))
adj_list = {i: [] for i in range(1, V+1)}  # 인접리스트  # 이 부분만 달라짐
visited = [0] * (V+1)

for i in range(E):
    s, e = temp[i*2], temp[i*2+1]
    adj_list[s].append(e)   # 가중치 없을 때 1
    adj_list[e].append(s)   # 방향성이 없음

bfs(1)
print(visited)  # [0, 1, 2, 2, 3, 3, 4, 3]

