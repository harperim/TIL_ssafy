import sys
sys.stdin = open('길찾기_input.txt')


def DFS(V):
    vis = [0] * (V + 1)
    stack = []
    vis[0] = 1
    v = 0
    while True:
        for w in abjL[v]:
            if vis[w] == 0:
                stack.append(w)
                v = w
                vis[v] = 1
                if v == 99:
                    return 1
                break
        else:
            if stack != []:
                v = stack.pop()
            else:
                break
    return 0


for _ in range(1, 11):
    tc, E = map(int, input().split())
    V = 99
    arr = list(map(int, input().split()))  # 입력은 2*E개
    abjL = [[] for _ in range(V + 1)]

    for i in range(E):
        v1, v2 = arr[i * 2], arr[i * 2 + 1]
        abjL[v1].append(v2)

    print(f'#{tc} {DFS(V)}')
