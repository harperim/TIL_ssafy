def perm(lev):
    # 1. 기저조건
    if lev == r:
        print(arr)
        return
    # 2. 유도파트
    for i in range(lev, n):
        arr[i], arr[lev] = arr[lev], arr[i]
        perm(lev + 1)
        arr[i], arr[lev] = arr[lev], arr[i]


arr = [1, 2, 3]
path = [0] * 2
n = len(arr)
r = 2
perm(0)
