import sys
sys.stdin = open('배열최소합_input.txt')


# 다른 사람 풀이
def perm(n, k, cursum):  # n : 최종 단계, k : 현재, cursum : 현재까지의 합
    global min_v
    if min_v < cursum:
        return
    if n == k:
        if min_v > cursum:
            min_v = cursum

    else:
        for i in range(k, n):
            idx[i], idx[k] = idx[k], idx[i]
            perm(n, k + 1, cursum + arr[k][idx[k]])
            idx[i], idx[k] = idx[k], idx[i]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    idx = [i for i in range(N)]

    min_v = 100
    perm(N, 0, 0)
    print(f'#{tc} {min_v}')
