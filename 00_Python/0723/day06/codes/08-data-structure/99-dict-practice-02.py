# 딕셔너리를 입력받아 value와 key를 뒤집은 결과를 반환하는 함수 `dict_invert()`를 작성하기


# # 1. [] 표기법을 사용한 방법
# def dict_invert(input_dict):
#     new_dict = {}
#     for key, value in input_dict.items():        # key, value 받아오기
#         #  딕셔너리 안에 없는 경우 -> value-key 값생성
#         if value not in new_dict:
#             new_dict[value] = [key]
#         #  딕셔너리 안에 있는 경우 -> value 키에 추가
#         else:
#             new_dict[value].append(key)
#     return new_dict


# # 2. get 메서드를 사용한 방법
# def dict_invert(input_dict):
#     new_dict = {}
#     for key, value in input_dict.items():
#         if new_dict.get(value) == None:
#             new_dict[value] = [key]
#         else:
#             new_dict[value].append(key)
#         # new_dict[value] = new_dict.get(value, []) + [key]  # extend
#     return new_dict


# 3. setdefault 메서드를 사용한 방법
def dict_invert(input_dict):
    new_dict = {}
    for key, value in input_dict.items():
        new_dict.setdefault(value, []).append(key)
    return new_dict

print(dict_invert({1: 10, 2: 20, 3: 30}))  # {10: [1], 20: [2], 30: [3]}
print(
    dict_invert({1: 10, 2: 20, 3: 30, 4: 30})
)  # {10: [1], 20: [2], 30: [3, 4]}
print(dict_invert({1: True, 2: True, 3: True}))  # {True: [1, 2, 3]}
