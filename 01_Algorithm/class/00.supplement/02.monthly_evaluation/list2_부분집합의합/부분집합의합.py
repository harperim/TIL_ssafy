import sys
sys.stdin = open('부분집합의합_input.txt')

# 테스트케이스 10개 중 6개 정답
# T = int(input())
#
# for tc in range(1, T+1):
#     n, k = list(map(int, input().split()))
#     answer = 0
#
#     for num in range(1, 13):
#         k -= num
#         n -= 1
#         if k == 0 and n == 0:
#             answer = 1
#             break
#
#     # print(answer)
#
#     if k > 0 and n > 0:
#         answer = 0
#     print(f'#{tc} {answer}')
"""
#1 1
#2 1
#3 0
"""

arr = list(range(1, 13))
n = len(arr)
T = int(input())
for tc in range(1, T+1):
    # N : 원소의 개수, K = 원소의 합
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, 1 << n):
        sum_val = 0
        cnt = 0
        for j in range(n):
            # i의 j번째 비트가 1이면
            if i & (1 << j):
                sum_val += arr[j]  # sum에 더한다.
                cnt += 1
        if sum_val == K and cnt == N:
            ans += 1
    print("#{} {}".format(tc, ans))

