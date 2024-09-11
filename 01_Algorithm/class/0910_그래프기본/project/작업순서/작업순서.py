import sys
sys.stdin = open('작업순서_input.txt')

# bfs, dfs 둘 다 상관 없음
# A형 2번 문제랑 유사

# 1
def dfs(v):
    visited[v] = 1
    ans.append(v)  # 정답
    for w in adj_list[v]:
        if not visited[w]:
            D[w] -= 1
            if D[w] == 0:
                dfs(w)


T = 10
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    tmp = list(map(int, input().split()))

    adj_list = [[] for _ in range(V + 1)]  # 인접리스트
    visited = [0] * (V + 1)
    D = [0] * (V + 1)
    for i in range(E):
        s, e = tmp[i * 2], tmp[i * 2 + 1]
        adj_list[s].append(e)
        D[e] += 1  # 가중치 증가

    ans = []
    while True:
        for i in range(1, V + 1):
            if D[i] == 0 and not visited[i]:
                dfs(i)
        if len(ans) == V:
            break
    print(f'#{tc}', *ans)



# 2
# def bfs():
#     Q = []
#     # 진입차수가 0인 정점을 enQ
#     for v in range(1, V + 1):
#         if D[v] == 0:
#             Q.append(v)
#             visited[v] = 1
#     while Q:
#         v = Q.pop(0)
#         ans.append(v)  # 할 일
#         for w in range(1, V + 1):  # 인접하고 미방문
#             if adj_mat[v][w] == 1 and visited[w] == 0:
#                 D[w] -= 1
#                 if D[w] == 0:
#                     Q.append(w)
#
#
# T = 10
# for tc in range(1, T + 1):
#     V, E = map(int, input().split())
#     tmp = list(map(int, input().split()))
#
#     adj_mat = [[0] * (V + 1) for _ in range(V + 1)]  # 인접행렬
#     visited = [0] * (V + 1)
#     D = [0] * (V + 1)  # 가중치
#     for i in range(E):
#         s, e = tmp[2 * i], tmp[2 * i + 1]
#         adj_mat[s][e] = 1
#         D[e] += 1  # 도착노드의 가중치를 증가
#
#     ans = []
#     bfs()
#     print(f'#{tc}', *ans)


