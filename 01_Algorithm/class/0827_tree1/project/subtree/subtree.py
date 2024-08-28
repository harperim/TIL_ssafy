import sys
sys.stdin = open('subtree_input.txt')

def preorder(v):
    global cnt
    if v:
        cnt += 1
        preorder(tree[v][0])
        preorder(tree[v][1])


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    V = E + 1
    tree = [[0] * 3 for _ in range(V+1)]
    temp = list(map(int, input().split()))
    for i in range(E):
        p, c = temp[i*2], temp[i*2+1]
        if tree[p][0] == 0:
            tree[p][0] = c
        else:
            tree[p][1] = c
        tree[c][2] = p
    cnt = 0
    preorder(N)
    print(f'#{tc} {cnt}')


