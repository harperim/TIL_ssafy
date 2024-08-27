import sys
sys.stdin = open('0729_구간합_input.txt', 'r')

T = int(input())

# for tc in range(1, T+1):  # 1 2 3
#     num_li = []
#     n, m = list(map(int, input().split()))
#     num = list(map(int, input().split()))
#     for idx in range(n-m+1):
#         num_li.append(sum(num[idx:idx+m]))
#
#     result = max(num_li) - min(num_li)
#     print(f'#{tc} {result}')

for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    max_v = 0
    min_v = 10_000_000

    for i in range(n-m+1):  # 0 1 2
        sum_v = 0
        for j in range(m):  # 0 1 2
            sum_v += arr[i+j]  # 0 1 2

        if max_v < sum_v:
            max_v = sum_v
        if min_v > sum_v:
            min_v = sum_v
    print(f'#{tc} {max_v-min_v}')


