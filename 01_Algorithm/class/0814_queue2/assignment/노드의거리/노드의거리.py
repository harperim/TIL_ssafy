import sys
sys.stdin = open('노드의거리_input.txt')

# 방향성 X
# enQ, deQ 순서 같으므로 원하는 위치에서 작업하면 됨

def bfs(v):
    Q = [v]  # Q 생성 및 endQ
    visited[v] = 1
    while Q:
        v = Q.pop(0)  # deQ
        # 해야할 일
        if v == goal:  # 할 일
            return visited[v] - 1
        for w in adj_list[v]:
            if visited[w] == 0:
                Q.append(w)
                visited[w] = visited[v] + 1
    return 0  # 경로에 없을 때


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj_list = [[] for _ in range(V+1)]  # 0번 인덱스 사용하지 않으므로
    visited = [0] * (V+1)
    for i in range(E):
        s, e = map(int, input().split())
        adj_list[s].append(e)
        adj_list[e].append(s)  # 방향성이 없기 때문에 2가지 경우 다 써주기

    start, goal = map(int, input().split())
    print(f'#{tc} {bfs(start)}')

