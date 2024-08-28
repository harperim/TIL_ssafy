'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''


def pre_order(v):
    global cnt  # 재귀니까 global로 하는게 편함
    if v != 0:
        print(v, end=' ')
        pre_order(tree[v][0])  # [0]번째가 왼쪽
        pre_order(tree[v][1])  # [1]번째는 오른쪽


def in_order(v):
    if v != 0:
        in_order(tree[v][0])  # [0]번째가 왼쪽
        print(v, end=' ')
        in_order(tree[v][1])  # [1]번째는 오른쪽


def post_order(v):
    if v != 0:
        post_order(tree[v][0])  # [0]번째가 왼쪽
        post_order(tree[v][1])  # [1]번째는 오른쪽
        print(v, end=' ')


def get_count(v):  # 전위순회
    global cnt
    if v != 0:
        cnt += 1
        get_count(tree[v][0])  # [0]번째가 왼쪽
        get_count(tree[v][1])  # [1]번째는 오른쪽


V = int(input())  # 정점의 개수
E = V - 1         # 간선의 개수 (주어질 때도 있고, 안 주어질 때도 있음)
temp = list(map(int, input().split()))

# 자리가 고정된 인접리스트
tree = [[0] * 3 for _ in range(V+1)]  # 정점의 개수 + 1만큼 범위 잡기

# 간선을 이용해서 인접리스트에 저장
for i in range(E):
    p, c = temp[i*2], temp[i*2+1]
    if tree[p][0] == 0:  # 왼쪽 자식이 없으면 (왼쪽을 먼저 집어넣겠다)
        tree[p][0] = c
    else:                # 왼쪽 자식이 있으면
        tree[p][1] = c

    tree[c][2] = p

# root 찾기
s = 13
while tree[s][2] != 0:
    s = tree[s][2]

pre_order(s)
print()
in_order(s)
print()
post_order(s)
print()

# 3번을 루트로 하는 노드의 개수
cnt = 0
get_count(3)
print(cnt)
