import sys
sys.stdin = open('그룹나누기_input.txt')

def find_set(x):
    if x == parent[x]:
        return x
    return find_set(parent[x])


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    parent = [i for i in range(N+1)]  # make set

    for i in range(M):
        s, e = arr[2*i], arr[2*i+1]
        # union
        parent[find_set(e)] = find_set(s)

    cnt = 0
    for i in range(1, N+1):
        if parent[i] == i:
            cnt += 1

    print(f'#{tc} {cnt}')

