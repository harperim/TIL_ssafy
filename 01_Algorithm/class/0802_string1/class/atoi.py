# atoi : ascii to integer (강사님이 외우는 방법! : array to integer)

def atoi(arr):  # arr = [1, 2, 3]
    value = 0
    for i in range(len(arr)):
        value = value * 10 + arr[i]
    return value

def itoa(num):  # num = 123
    arr = []
    while num:
        arr.append(num % 10)  # 맨 마지막 값 잘라오기 / 123 % 10 = 3 / 12 % 10 = 2 / 1 % 10 =
        num = num // 10  # 123//10 = 12  / 12//10 = 1
    arr.reverse()
    return arr


a = '123'
a = [1, 2, 3]
b = atoi(a)

