def comb(level, start):
    if level == R:
        print(path)
        return
    for i in range(start, N):
        path.append(arr[i])
        comb(level+1, start+1)
        path.pop()


arr = [1, 2, 3, 4]
N = len(arr)
R = 3
path = []
comb(0, 0)
