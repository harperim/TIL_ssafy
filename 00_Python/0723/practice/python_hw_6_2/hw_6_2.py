# 아래 함수를 수정하시오.
def remove_duplicates_to_set(lst):
    return set(lst)

def remove_duplicates_to_set2(lst):
    new_lst = []        # 중복제거 리스트에 저장
    for num in lst:     # 리스트를 순회
        # new_lst에 포함되여있지 않으면 추가
        if num not in new_lst:
            new_lst.append(num)
    return set(new_lst)


result = remove_duplicates_to_set([1, 2, 2, 3, 4, 4, 5])
print(result)

result = remove_duplicates_to_set2([1, 2, 2, 3, 4, 4, 5])
print(result)
