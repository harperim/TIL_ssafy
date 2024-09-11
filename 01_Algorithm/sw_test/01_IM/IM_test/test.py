'''
1
5
0 0 0 1 0
0 1 0 1 0
0 0 1 0 2
1 0 0 1 0
0 1 0 1 0
'''

# 사각지대 개수를 구해라 (0의 개수)
# 0 통로 / 1 벽 / 2 경비원
# 상하좌우로만 이동 가능

import sys
sys.stdin = open('test_input.txt')

# 1. visited 사용한 방법
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            # 벽인 경우(1)에도 1로 방문 처리
            if arr[i][j] == 1:
                visited[i][j] = 1
            # 경비원인 경우(2), 그 위치에서 탐색 시작
            if arr[i][j] == 2:
                visited[i][j] = 1
                for k in range(4):
                    for l in range(1, N+1):
                        nx = i + dx[k] * l
                        ny = j + dy[k] * l
                        if 0 <= nx < N and 0 <= ny < N:
                            if visited[nx][ny] == 1:
                                break
                            elif visited[nx][ny] == 0:
                                visited[nx][ny] = 1

    cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                cnt += 1
    print(f'#{tc} {cnt}')

# 2. visited 사용하지 X 방법
# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     for i in range(N):
#         for j in range(N):
#             # 경비원인 경우(2), 그 위치에서 탐색 시작
#             if arr[i][j] == 2:
#                 arr[i][j] = 1
#                 for k in range(4):
#                     for l in range(1, N+1):
#                         nx = i + dx[k] * l
#                         ny = j + dy[k] * l
#                         if 0 <= nx < N and 0 <= ny < N:
#                             if arr[nx][ny] == 1:
#                                 break
#                             elif arr[nx][ny] == 0:
#                                 arr[nx][ny] = 1
#
#     cnt = 0
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 0:
#                 cnt += 1
#     print(f'#{tc} {cnt}')


