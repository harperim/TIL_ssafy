# for문으로 쉽게 중복순열 만들기 (0부터 시작)
# for i in range(3):
#     for j in range(3):
#         for k in range(3):
#             print(i, j, k)

# --------------------
def perm(lev):
    if lev == N:
        print(path)
        return
    for i in range(N):
        if visited[i]: continue
        visited[i] = 1
        path.append(arr[i])
        perm(lev+1)
        path.pop()
        visited[i] = 0

path = []
arr = [1, 2, 3]
N = len(arr)
visited = [0] * N
perm(0)

