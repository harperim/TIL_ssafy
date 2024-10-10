import sys
sys.stdin = open('최장경로_input.txt', 'r')


def dfs(v, count):
    # 깊이 우선 탐색(DFS) 함수
    global max_count  # 최장 경로 길이를 저장할 전역 변수
    visited[v] = True  # 현재 노드를 방문 처리

    # 현재 노드와 연결된 모든 인접 노드에 대해 탐색
    for i in graph[v]:
        if visited[i] == False:  # 방문하지 않은 노드인 경우
            dfs(i, count + 1)  # 해당 노드로 재귀 호출, 경로 길이 증가

    visited[v] = False  # 백트래킹: 노드를 다시 미방문 상태로 변경

    # 현재까지의 경로 길이가 최장 경로보다 길다면 업데이트
    if count > max_count:
        max_count = count


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 노드 수 N / 간선 수 M

    # 각 노드의 인접 리스트를 위한 배열 초기화
    graph = [[] for _ in range(N + 1)]
    # 방문 처리 배열 초기화
    visited = [False] * (N + 1)

    # 간선 정보 입력
    for i in range(M):
        x, y = map(int, input().split())
        graph[x].append(y)  # x에서 y로 가는 간선 추가
        graph[y].append(x)  # y에서 x로 가는 간선 추가 (무향 그래프)

    # 최장 간선의 길이 구하기
    count, max_count = 0, 0  # 초기 경로 길이 설정

    # 각 노드를 시작점으로 DFS 수행
    for i in range(1, N + 1):
        dfs(i, 1)  # 시작 노드와 초기 경로 길이 1로 DFS 호출

    # 최장 경로의 길이를 출력
    print(f'#{tc} {max_count}')
