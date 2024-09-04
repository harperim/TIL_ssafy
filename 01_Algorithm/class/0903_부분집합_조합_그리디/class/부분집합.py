def powerset(lev):
    if lev == N:
        print(bit)
        return

    bit[lev] = 1
    powerset(lev+1)
    bit[lev] = 0
    powerset(lev+1)

arr = [1, 2, 3]
N = len(arr)
bit = [0] * N
powerset(0)
