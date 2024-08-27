# 풍선팡

import sys
sys.stdin = open("9490_input.txt")

# T = int(input())
#
# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]
#
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     max_v = 0
#
#     for i in range(N):
#         for j in range(M):
#             sum_v = 0
#             sum_v += arr[i][j]
#             current_cnt = arr[i][j]
#
#             for l in range(1, current_cnt+1):
#                 for k in range(4):
#                     nx = i + dx[k]*l
#                     ny = j + dy[k]*l
#
#                     if 0 <= nx < N and 0 <= ny < M:
#                         sum_v += arr[nx][ny]
#
#             if max_v < sum_v:
#                 max_v = sum_v
#
#     print(f'#{tc} {max_v}')

# 강사님 코드
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # 행, 열 크기
    arr = [list(map(int, input().split())) for _ in range(N)]  # 풍선별 꽃가루 수

    max_v = 0       # 꽃가루 최대 합계
    for i in range(N):  # 터트릴 풍선의 위치
        for j in range(M):
            cnt = arr[i][j]  # 터트린 풍선에서 나오는 꽃가루 개수
            # 주변 풍선의 꽃가루 수
            for k in range(4):  # 확인할 방향
                for l in range(1, arr[i][j]+1):       # 주변 방향으로 추가로 터지는 풍선과의 거리
                    ni = i + di[k] * l
                    nj = j + dj[k] * l

                    if 0 <= ni < N and 0 <= nj < M:
                        cnt += arr[ni][nj]

            if max_v < cnt:
                max_v = cnt

    print(f'#{tc} {max_v}')
