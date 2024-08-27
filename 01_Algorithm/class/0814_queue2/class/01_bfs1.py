'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

# 외워질 때까지 연습하기
def bfs(s, V):      # 시작점 s, 마지막 정점 V
    # 준비
    visited = [0] * (V+1)       # visited 생성 (visit(t) => 경로출력 역할 )
    q = []                      # 큐 생성
    q.append(s)                 # 시작점 인큐
    visited[s] = 1              # 시작점 방문(인큐됨) 표시

    # 탐색
    while q:        # 탐색할 정점이 남아있으면
        t = q.pop(0)        # t <- deque
        print(t)            # 처리
        for w in adj_l[t]:      # t에 인접하고, 인큐된 적이 없으면
            if visited[w] == 0:
                q.append(w)     # 인큐하고 인큐 표시
                visited[w] = 1
    print(visited)


V, E = map(int, input().split())  # V 마지막 정점 번호
arr = list(map(int, input().split()))
adj_l = [[] for _ in range(V+1)]  # [[], [], [], ...]

for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)        # 방향이 없는 경우

bfs(2, V)
# bfs(2, V)       # 출발점, 정점수
