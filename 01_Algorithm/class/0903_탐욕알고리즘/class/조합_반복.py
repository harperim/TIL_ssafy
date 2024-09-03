arr = list(range(6))
N = len(arr)
for i in range(0, N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            print(i, j, k)
