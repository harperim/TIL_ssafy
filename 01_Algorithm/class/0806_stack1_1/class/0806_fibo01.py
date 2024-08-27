def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)


print(fibo(950))    # maximum recursion = 1000개 / 1000 입력하면 에러남
