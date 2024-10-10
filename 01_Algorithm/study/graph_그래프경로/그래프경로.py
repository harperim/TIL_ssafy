import sys
sys.stdin = open('그래프경로_input.txt')


def dfs(S, G):
    # 깊이 우선 탐색(DFS) 함수
    stack = []  # 스택 초기화
    stack.append(S)  # 시작 노드를 스택에 추가

    while stack:
        v = stack.pop()  # 스택에서 노드를 꺼냄

        if visited[v] == 0:  # 아직 방문하지 않은 노드인 경우
            visited[v] = 1  # 노드를 방문 처리

            for w in range(1, V + 1):  # 인접 노드를 순회
                if graph[v][w] == 1 and visited[w] == 0:  # 인접하고 아직 방문하지 않은 노드
                    if w == G:  # 목표 노드에 도달한 경우
                        return 1  # 경로가 존재함을 나타냄
                    stack.append(w)  # 인접 노드를 스택에 추가

    return 0  # 경로가 존재하지 않을 경우 0 반환


# 테스트 케이스 수 입력
T = int(input())
for tc in range(1, T+1):
    # 정점 수 V와 간선 수 E 입력
    V, E = map(int, input().split())

    # 방문 배열 초기화 (1-indexed)
    visited = [0 for _ in range(V + 1)]
    # 인접 행렬 초기화 (1-indexed)
    graph = [[0 for _ in range(V + 1)] for _ in range(V + 1)]

    # 간선 정보 입력
    for _ in range(E):
        i, j = map(int, input().split())
        graph[i][j] = 1  # i에서 j로 가는 간선 추가 (무향 그래프가 아닌 경우)

    # 시작 노드 S와 목표 노드 G 입력
    S, G = map(int, input().split())
    # DFS를 실행하여 경로의 존재 여부를 확인하고 결과 출력
    print(f'#{tc}', dfs(S, G))
