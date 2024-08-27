import sys
sys.stdin = open('회문_input.txt')

"""
for i in range(N):
    for j in range(N-M+1):
        flag = 1
        for k in range(M//2):
            if a[i][j+k] != a[i][j+M-1]:
                flag = 0
                break
        if flag:
            출력
"""

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    result = []

    for i in range(N):
        for j in range(N - M + 1):
            f1 = f2 = 1
            for k in range(M // 2):
                if arr[i][j + k] != arr[i][j + M - 1 - k]:  # 행 기준 탐색
                    f1 = 0
                if arr[j + k][i] != arr[j + M - 1 - k][i]:  # 열 기준 탐색
                    f2 = 0
            if f1:  # 행을 기준으로 봤을 때 답을 찾은 경우
                result += arr[i][j:j + M]
            if f2:  # 열을 기준으로 봤을 때 답을 찾은 경우
                result += (arr[j + k][i] for k in range(M))

    answer = ''.join(result)
    print(f'#{tc} {answer}')


# # 강사님 풀이
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [list(input()) for _ in range(N)]
#
#     # 가로 방향
#     print(f'#{tc}', end=' ')
#     for i in range(N):
#         for j in range(N-M+1):
#             flag = True
#             for k in range(M//2):
#                 if arr[i][j+k] != arr[i][j+M-1-k]:  # k번 비교해야 해서 앞에 +k, 뒤에 -k
#                     flag = False
#                     break
#             if flag:
#                 for k in range(M):
#                     print(f'{arr[i][j+k]}', end='')
#                 print()
