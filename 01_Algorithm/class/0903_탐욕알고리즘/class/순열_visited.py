# for문으로 쉽게 중복순열 만들기 (0부터 시작)
# for i in range(3):
#     for j in range(3):
#         for k in range(3):
#             print(i, j, k)

# --------------------
def PI(lev):
    if lev == N:
        print(path)
        return
    for i in range(N):
        path.append(arr[i])
        PI(lev+1)
        path.pop()

path = []
arr = [1, 2, 3]
N = len(arr)
PI(0)

