# 내가 푼 문제 : 다시 풀어보기 (아직 완성되지 않음)

import sys
sys.stdin = open('sum_input.txt')

T = 10

max_v = 0
# for tc in range(1, T+1):
#     n = int(input())
#     lst = [list(map(int, input().split())) for _ in range(100)]
#
#     for i in range(100):
#         sum_row = 0
#         sum_col = 0
#         sum_l_cross = 0
#         sum_l_cross += lst[i][i]
#         if sum_l_cross > max_val:
#             max_val = sum_l_cross
#         for j in range(100):
#             sum_row += lst[i][j]
#             sum_col += lst[j][i]
#             if sum_row > max_val:
#                 max_val = sum_row
#             if sum_col > max_val:
#                 max_val = sum_col
#
#     for i in range(100):
#         sum_r_cross = 0
#         sum_r_cross += lst[i][100 - (i + 1)]
#         if sum_r_cross > max_val:
#             max_val = sum_r_cross
#     print(f'#{tc} {max_val}')


for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    sum_l_cross = 0
    sum_r_cross = 0
    for i in range(100):
        sum_row = 0
        sum_col = 0
        sum_l_cross += arr[i][i]
        sum_r_cross += arr[i][100-1-i]

        if max_v < sum_l_cross:
            max_v = sum_l_cross
        if max_v < sum_r_cross:
            max_v = sum_r_cross
        for j in range(100):
            sum_row += arr[i][j]
            sum_col += arr[j][i]
        # 최대값
        if max_v < sum_row:
            max_v = sum_row
    print(f'#{tc} {max_v}')
