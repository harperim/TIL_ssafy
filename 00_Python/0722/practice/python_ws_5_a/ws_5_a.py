N = 9
data_1 = '123456789'
arr_0 = list(data_1)
print(arr_0)
arr_1 = []
# 아래에 코드를 작성하시오.
for ch in data_1:
    arr_1.append(ch)
print(arr_1)



M = 15
data_2 = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15'
# 아래에 코드를 작성하시오.
arr_2 = data_2.split()
# print(arr_2)
for ch in arr_2:
    if int(ch) % 2 == 1:
        print(ch)