def get_sum(a):
    sum_v = 0   # 합을 저장할 변수를 초기화
    # 1. 값저장
    for num in a:
        sum_v = sum_v + num  
        # sum_v += num
    # 2. 인덱스
    # for i in range(len(a)): # 0 1 2 3 4
    #     sum_v += a[i]
    return sum_v

def get_min(a):
    min_v = a[0]   # 첫번째 요소, 큰값(min_v = 987654321)
    for num in a:
        if min_v > num:
            min_v = num
    return min_v

def get_max(a):
    max_v = a[0]   # 첫번째 요소, 작은값(min_v = -987654321)
    for num in a:
        if max_v < num:
            max_v = num
    return max_v

def get_len(a):
    count = 0
    for num in a:
        count += 1
    return count

def get_max_idx(a):
    max_idx = 0  # 첫번째 인덱스를 최대값으로 가정
    for i in range(1, len(a)):  # 두번째 인덱스 부터 검사
        if a[max_idx] < a[i]:
            max_idx = i
    return max_idx, a[max_idx]

arr = [1, 2, 3, 4, 5]
print(get_sum(arr))
print(get_min(arr))
print(get_max(arr))
print(get_len(arr))
# avg
print(get_sum(arr) / get_len(arr))
max_i, max_v = get_max_idx(arr)
print(max_i, max_v)