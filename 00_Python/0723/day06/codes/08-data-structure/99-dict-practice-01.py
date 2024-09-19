# 각 혈액형의 인원수를 계산하는 딕셔너리를 생성하기.
blood_types = ['A', 'B', 'O', 'AB', 'A', 'O', 'B', 'A', 'AB', 'O', 'A', 'B']


# 1. [] 표기법을 사용한 방법
def count_blood_types(blood_types):
    my_dict = {}                # 딕셔너리 초기화
    for blood in blood_types:   # blood_types를 for문으로 순회
        if blood in my_dict:       # 혈액형이 딕셔너리에 존재하면
            my_dict[blood] += 1         # 1증가
        else:                       # 존재하지 않으면
            my_dict[blood] = 1
    return my_dict              # 딕셔너리 반환

print(count_blood_types(blood_types))  # {'A': 4, 'B': 3, 'O': 3, 'AB': 2}


# 2. get() 메서드를 사용한 방법
def count_blood_types(blood_types):
    my_dict = {}                # 딕셔너리 초기화
    for blood in blood_types:   # blood_types를 for문으로 순회
        if my_dict.get(blood):       # 혈액형이 딕셔너리에 존재하면
            my_dict[blood] += 1         # 1증가
        else:                       # 존재하지 않으면
            my_dict[blood] = 1
        # my_dict[blood] = my_dict.get(blood, 0) + 1
    return my_dict              # 딕셔너리 반환


print(count_blood_types(blood_types))  # {'A': 4, 'B': 3, 'O': 3, 'AB': 2}
