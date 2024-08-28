'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

V = int(input())  # 정점의 개수
E = V-1           # 간선의 개수
temp = list(map(int, input().split()))
tree = [[0] * 3 for _ in range(V+1)]  # 자리가 고정된 인접 리스트

# 간선을 이용해서 인접 리스트에 저장
for i in range(E):
    p, c = temp[i*2], temp[i*2+1]
    if tree[p][0] == 0:     # 왼쪽 자식이 없으면
        tree[p][0] = c
    else:                   # 왼쪽 자식이 있으면
        tree[p][1] = c
    tree[c][2] = p          # 부모 노드

# 루트 찾기
root = 13                 # 임의로 지정
while tree[root][2]:
    root = tree[root][2]  # 부모 노드로 거슬러 올라감


# 전위 순회
def pre_order(v):
    if v != 0:
        print(v, end='')
        pre_order(tree[v][0])       # 왼쪽 자식 노드
        pre_order(tree[v][1])       # 오른쪽 자식 노드


# 중위 순회
def in_order(v):
    if v != 0:
        in_order(tree[v][0])  # 왼쪽 자식 노드
        print(v, end='')
        in_order(tree[v][1])  # 오른쪽 자식 노드


# 후위 순회
def post_order(v):
    if v != 0:
        post_order(tree[v][0])  # 왼쪽 자식 노드
        post_order(tree[v][1])  # 오른쪽 자식 노드
        print(v, end='')


# 전위 순회하면서 노드 개수 세기
def get_count(v):
    global cnt
    if v != 0:
        cnt += 1
        get_count(tree[v][0])  # 왼쪽 자식 노드
        get_count(tree[v][1])  # 오른쪽 자식 노드


pre_order(root)
print()
in_order(root)
print()
post_order(root)
print()

# 3번을 루트로 시작하여 전위 순회할 때 거쳐가는 노드의 개수
cnt = 0
get_count(3)
print(cnt)

