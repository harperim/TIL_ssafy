import sys
sys.stdin = open('배열최소합_input.txt')



# 순열 문제 파악되면 바로 순열 구하기 시작
# A형 치고 쉬운 문제

# 1. 시간 초과 나는 경우
# T = int(input())
# def perm(n, k, cursum):     # cursum 매개변수 추가
#     global ans
#
#     if n == k:
#         sum_v = 0
#         for i in range(n):
#             sum_v += arr[i][order[i]]
#         if ans > sum_v:
#             ans = sum_v
#     else:
#         for i in range(k, n):
#             order[i], order[k] = order[k], order[i]
#             perm(n, k + 1)
#             order[i], order[k] = order[k], order[i]
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     ans = 987654321
#     order = list(range(N))  # [i for i in range(N)]
#     perm(N, 0)      # 매개변수 전달
#     print(f'#{tc} {ans}')


# 2. 가지치기 시행한 경우
def perm(n, k, cursum):  # cursum 매개변수 추가
    global ans
    if ans < cursum: return

    if n == k:
        sum_v = 0
        for i in range(n):
            sum_v += arr[i][order[i]]
        if ans > sum_v:
            ans = sum_v
    else:
        for i in range(k, n):
            order[i], order[k] = order[k], order[i]
            perm(n, k + 1, cursum + arr[k][order[k]])  # 어떤값을 cursum에 넘겨줄지 고민???
            order[i], order[k] = order[k], order[i]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 987654321
    order = list(range(N))  # [i for i in range(N)]
    perm(N, 0, 0)  #
    print(f'#{tc} {ans}')
