def powerset(n, k):     # n : 최종, k : 현재
    if n == k:
        print(bit)
        for i in range(n):
            if bit[i]:
                print(arr[i], end=' ')
    else:
        bit[k] = 1
        powerset(n, k + 1)
        bit[k] = 0
        powerset(n, k + 1)


N = 3
arr = [1, 2, 3]
bit = [0] * N
powerset(N, 0)

