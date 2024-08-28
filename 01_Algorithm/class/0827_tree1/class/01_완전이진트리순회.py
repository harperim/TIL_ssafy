# 완전이진트리

tree = [0, 1, 2, 3, 4, 5, 6, 7]

def pre_order(v):
    if v <= N:  # 노드의 개수보다 정점번호가 작으면
        print(tree[v])  # 루트
        pre_order(2 * v)  # 현재 정점에서 *2 하면 => 왼쪽 자식
        pre_order(2 * v + 1)  # 오른쪽 자식


N = 7  # 노드의 개수
E = N - 1
pre_order(1)
