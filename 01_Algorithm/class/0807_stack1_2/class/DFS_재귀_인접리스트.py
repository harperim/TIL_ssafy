# 강사님 풀이
"""
1
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
"""

def dfs(v):
    visited[v] = 1          # 방문체크
    print(v, end=' ')

    # 시작정점(v)에 인접한 정점(w) 중에 방문 안 한 정점
    for w in adj_list[v]:
        if visited[w] == 0:      # w가 방문하지 않았으면
            dfs(w)


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj_list = [[] for _ in range(V+1)]     # 인접리스트 초기화
    visited = [0] * (V+1)                           # 방문체크
    temp = list(map(int, input().split()))

    # 인접행렬 저장하기
    for i in range(E):
        s, e = temp[i*2], temp[i*2+1]
        print(s, e)
        adj_list[s].append(e)
        adj_list[e].append(s)
    print(adj_list)
