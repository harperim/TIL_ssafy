# greedy_1이될때까지

import sys
sys.stdin = open('input.txt', 'r')

N, K = list(map(int, input().split()))  # 17, 4
count = 0

# N = 1이 되는 순간 멈추기
while N != 1:
    if N % K == 0:
        N //= K
        count += 1
    else:
        N -= 1
        count += 1
print(count)

