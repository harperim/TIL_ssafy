import sys
import heapq
sys.stdin = open('shorted_input.txt')


def initialize(max_n):
    # 최대 노드 수에 맞춰 거리 배열 초기화
    return [float('inf')] * max_n


def input_graph(m):
    # m개의 간선을 가진 그래프를 입력받아 생성
    graph = [[] for _ in range(n + 1)]  # n + 1 크기의 그래프 생성 (0-indexed)
    for _ in range(m):
        # 각 간선의 정보를 입력받아 그래프에 추가
        a, b, c = map(int, input().split())  # a와 b는 노드, c는 거리
        graph[a].append((b, c))  # a에서 b로 가는 간선 추가
        graph[b].append((a, c))  # b에서 a로 가는 간선 추가 (무향 그래프)
    return graph


def dijkstra(start, end, graph, n):
    # 다익스트라 알고리즘을 사용하여 start에서 end까지의 최단 경로를 계산
    dist = initialize(n + 1)  # n + 1 크기로 거리 배열 초기화
    dist[start] = 0  # 시작 노드의 거리는 0
    pq = [(0, start)]  # (비용, 노드) 형태의 우선순위 큐 초기화

    while pq:
        # 큐에서 가장 비용이 적은 노드를 꺼냄
        cost, cur = heapq.heappop(pq)

        # 이미 기록된 거리보다 큰 경우 무시
        if cost > dist[cur]:
            continue

        # 현재 노드와 연결된 노드들 탐색
        for next_node, n_cost in graph[cur]:
            # 더 짧은 경로 발견 시 거리 업데이트
            if dist[next_node] > cost + n_cost:
                dist[next_node] = cost + n_cost
                # 업데이트된 거리를 우선순위 큐에 추가
                heapq.heappush(pq, (dist[next_node], next_node))

    return dist[end]  # 목표 노드까지의 최단 거리 반환


def solve():
    global n
    tc = int(input())
    for t in range(1, tc + 1):
        # 각 테스트 케이스에 대한 노드 수, 간선 수, 시작 노드, 종료 노드 입력
        n, m, start, end = map(int, input().split())
        graph = input_graph(m)  # 그래프 생성
        answer = dijkstra(start, end, graph, n)  # 최단 경로 계산
        print(f"#{t} {answer}")


solve()
