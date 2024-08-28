import sys
sys.stdin = open('이진탐색_input.txt')

# def inorder(node):
#     global cnt
#     if node <= N:
#         inorder(node * 2)
#         tree[node] = cnt
#         cnt += 1
#         inorder(node * 2 + 1)
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     tree = [0] * (N + 1)  # 7
#     cnt = 1
#
#     inorder(1)
#     print(f'#{tc} {tree[1]} {tree[N // 2]}')


# 강사님 풀이
def inorder(v):
    global num
    if v <= N:
        inorder(v * 2)  # 왼쪽 자식
        tree[v] = num  # 할일
        num += 1
        inorder(v * 2 + 1)  # 오른쪽 자식


T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 마지막 노드 값
    tree = [0] * (N + 1)  # 0번 인덱스 사용 안 함
    num = 1
    inorder(1)
    print(f'#{tc} {tree[1]} {tree[N // 2]}')  # 루트는 항상 1번
