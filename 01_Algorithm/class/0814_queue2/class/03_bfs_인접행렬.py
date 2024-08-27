'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''


def bfs(v):
    # enQ + 방문체크
    Q = []
    Q.append(v)  # -> Q = [v]
    visited[v] = 1
    print(v, end=' ')  # 1

    while Q:
        v = Q.pop(0)     # v = deQ
        # 시작정점(v)의 인접하고 방문 안 한 정점(w)
        for w in range(1, V+1):
            if adj_mat[v][w] == 1 and visited[w] == 0:
                # enQ + 방문체크
                Q.append(w)
                visited[w] = visited[v] + 1


V, E = map(int, input().split())
temp = list(map(int, input().split()))
adj_mat = [[0] * (V+1) for _ in range(V+1)]  # 인접행렬
visited = [0] * (V+1)

for i in range(E):
    s, e = temp[i*2], temp[i*2+1]
    adj_mat[s][e] = 1       # 가중치 없을 때 1
    adj_mat[e][s] = 1       # 방향성이 없음

bfs(1)
print(visited)  # [0, 1, 2, 2, 3, 3, 4, 3]


# 시작정점(1)에서 가장 멀리 떨어져 있는 정점의 번호와 사이의 간선의 개수를 출력하시오.
# 정답 : 6 3
# visited 안에 다 들어있음
# 값이 가장 큰 놈이 멀리 떨어져 있음
max_i = 0
for i in range(len(visited)):
    if visited[max_i] < visited[i]:
        max_i = i
print(max_i, visited[max_i]-1)

# 유사 문제 : 가장 나중에 연락 받는 친구는 누구냐
# visited 의 값이 가장 큰 친구
