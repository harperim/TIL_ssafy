import sys
sys.stdin = open('최소생산비용_input.txt')


def perm(lev, cursum):
    global ans
    if ans <= cursum:
        return

    if lev == N:
        if ans > cursum:
            ans = cursum
        return

    for i in range(N):
        if visited[i]: continue
        visited[i] = 1
        path.append(i)
        perm(lev + 1, cursum + arr[lev][i])
        path.pop()
        visited[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    path = []
    visited = [0] * N
    ans = 0xffffffff
    perm(0, 0)
    print(f'#{tc} {ans}')


