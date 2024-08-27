import sys
sys.stdin = open('그래프경로_input.txt')

# 전역변수에서 정의된 변수 중에서 함수 내에서
# 참조형(list) 변수는 읽기 쓰기
# 값형(불변, int, string) 변수는 읽기만 가능,
    # 쓰기를 하고 싶으면 global로 재정의

# adj_list = [[], [4, 3], [3, 5],[], [6], [], []]
# s, g = 1, 6

def dfs(v):
    global flag
    visited[v] = 1  # 방문체크
    # 하고싶은일
    if v == G:
        flag = 1
        return

    # v의 인접정점(w)중에서 방문 안 한 정점
    for w in adj_list[v]:
        if visited[w] == 0:
            dfs(w)  # w로 재귀호출


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adj_list = [[] for _ in range(V + 1)]  # 인접리스트 초기화
    visited = [0] * (V + 1)
    for _ in range(E):  # 간선수만큼 반복
        s, e = map(int, input().split())
        adj_list[s].append(e)
    S, G = map(int, input().split())  # 시작, 도착
    flag = 0  # (2) flag를 이용
    dfs(S)
    print(f'#{tc} {flag}')


