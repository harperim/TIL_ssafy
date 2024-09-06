import sys
sys.stdin = open('전기버스2_input.txt')


def dfs(level, e, cnt):
    global ans
    # 0. 가지치기
    # 1. 기저조건
    if level == N:
        ans = min(ans, cnt)
        return
    # 2. 유도파트
    # 충전을 하는 경우
    dfs(level + 1, arr[level]-1, cnt + 1)
    # 충전을 하지 않는 경우
    if e > 0:
        dfs(level+1, e-1, cnt)


T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = arr[0]
    ans = N
    dfs(2, arr[1]-1, 0)
    print(f'#{tc} {ans}')
