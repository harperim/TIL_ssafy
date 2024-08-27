import sys
sys.stdin = open('0729_minmax_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_val = 0
    min_val = 987654321

    for val in arr:
        if max_val < val:
            max_val = val
        if min_val > val:
            min_val = val

    result = max_val - min_val
    print(f'#{tc} {result}')

