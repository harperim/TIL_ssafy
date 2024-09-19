# 아래 함수를 수정하시오.
def find_min_max(arr):
    return min(arr), max(arr)


def find_min_max2(arr):
    min_v = arr[0]
    max_v = arr[0]
    for num in arr:
        if min_v > num:
            min_v = num
        if max_v < num:
            max_v = num
    return min_v, max_v


result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)

result = find_min_max2([3, 1, 7, 2, 5])
print(result)  # (1, 7)
