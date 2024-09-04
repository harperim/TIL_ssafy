# 4+4 방향 탐색
# 2차원 배열 순회 (2 for + for)
# 4방향 (for)
# 세기 (for)
# => 4중 for문

import sys
sys.stdin = open('파리퇴치3_input.txt')


def get_sum(x, y, dx, dy):  # 4방향탐색의 합
    sum_v = arr[x][y]
    for m in range(1, M):  # 세기
        for i in range(4):  # 4방향
            nx = x + dx[i] * m
            ny = y + dy[i] * m
            # 인덱스체크
            if 0 <= nx < N and 0 <= ny < N:
                sum_v += arr[nx][ny]
    return sum_v


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dx2 = [-1, 1, 1, -1]
dy2 = [1, 1, -1, -1]
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    # 2차원 배열 순회
    for i in range(N):
        for j in range(N):
            s1 = get_sum(i, j, dx, dy)
            if max_v < s1:
                max_v = s1
            s2 = get_sum(i, j, dx2, dy2)
            if max_v < s2:
                max_v = s2
    print(f'#{tc} {max_v}')
