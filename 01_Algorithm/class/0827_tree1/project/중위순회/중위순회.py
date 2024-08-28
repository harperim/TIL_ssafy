import sys
sys.stdin = open('중위순회_input.txt')

# 강사님 풀이1
def inorder(v):
    global ans
    if v <= N:
        inorder(2*v)
        ans += tree[v]
        inorder(2*v+1)


T = 10
for tc in range(1, T+1):
    N = int(input())
    tree = [''] * (N+1)
    for i in range(N):
        tmp = list(input().split())
        idx = int(tmp[0])
        tree[idx] = tmp[1]

    ans = ''
    inorder(1)

    print(f'#{tc} {ans}')
