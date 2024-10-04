import sys
sys.stdin = open('보급로_input.txt')

from collections import deque

# 상하좌우
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(arr, visited, time, S, G):
    deq = deque([S])
    while deq:
        x, y = deq.popleft()  # 큐에서 현재 위치 x, y 꺼내기
        for k in range(4):  # 상하좌우 탐색
            nx = x + dx[k]  # 새로운 좌표 x
            ny = y + dy[k]  # 새로운 좌표 y
            if 0 <= nx < N and 0 <= ny < N:
                if nx == 0 and ny == 0:  # 시작점 제외
                    continue
                elif visited[nx][ny] == 0:  # 방문하지 않은 경우
                    visited[nx][ny] = 1     # 방문 처리
                    time[nx][ny] = time[x][y] + arr[nx][ny]  # 현재 위치까지의 시간에 가중치 더해서 저장하기
                    deq.append((nx, ny))  # 새로운 좌표 큐에 추가
                else:  # 방문한 경우
                    if time[nx][ny] > time[x][y] + arr[nx][ny]:  # 더 짧은 경로 발견 시
                        time[nx][ny] = time[x][y] + arr[nx][ny]  # 시간 업데이트
                        deq.append((nx, ny))  # 큐에 추하여 다시 탐색 시작


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(list(map(int, input())) for _ in range(N))

    visited = [[0] * N for _ in range(N)]
    time = [[0] * N for _ in range(N)]
    S, G = [0, 0], [N - 1, N - 1]

    bfs(arr, visited, time, S, G)
    answer = time[G[0]][G[1]]

    print(f'#{tc} {answer}')