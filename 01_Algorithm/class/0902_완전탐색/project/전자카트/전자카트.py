import sys
sys.stdin = open('전자카트_input.txt')


def perm(lev, cursum):
    global ans
    if lev == N:
        cursum += arr[path[N - 1]][path[0]]  # 마지막-> 0 으로 가는 거리 추가
        if ans > cursum:
            ans = cursum
        return

    for i in range(1, N):  # 출발점을 제외하고
        if visited[i]: continue
        visited[i] = 1
        path.append(i)
        perm(lev + 1, cursum + arr[path[lev - 1]][path[lev]])
        path.pop()
        visited[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    path = [0]  # 출발점을 넣고 시작
    visited = [0] * N
    visited[0] = 1  # 출발점 방문 표시
    ans = 987654321
    perm(1, 0)  # lev 0를 제외
    print(f'#{tc} {ans}')


# 2 풀이
def perm(lev, cursum):
    global ans
    if ans < cursum: return

    if lev == N:
        cursum += arr[path[N - 1]][path[0]]  # 마지막-> 0 으로 가는 거리 추가
        if ans > cursum:
            ans = cursum
        return

    for i in range(1, N):  # 출발점을 제외하고
        if visited[i]: continue
        visited[i] = 1
        path.append(i)
        perm(lev + 1, cursum + arr[path[lev - 1]][path[lev]])
        path.pop()
        visited[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    path = [0]  # 출발점을 넣고 시작
    visited = [0] * N
    visited[0] = 1  # 출발점 방문 표시
    ans = 987654321
    perm(1, 0)  # lev 0를 제외
    print(f'#{tc} {ans}')

