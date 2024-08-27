import sys
sys.stdin = open('글자수_input.txt')

T = int(input())

for tc in range(1, T+1):
    str1 = str(input())
    str2 = str(input())

    dict_letter = {}

    # 1. 중복되는 str1 값 제거하기
    for letter in str1:
        dict_letter[letter] = 0     # 키값이 없으면 추가, 있으면 갱신

    # 2. 저장한 keys 값을 기준으로 개수 세서 딕셔너리에 저장하기
    for key in dict_letter.keys():  # X Y P V
        for spell in str2:  # E O G G X Y P V S Y
            if key == spell:
                if key not in dict_letter:
                    dict_letter[key] = 1
                else:
                    dict_letter[key] += 1

    # 3. 가장 긴 문자열 길이 찾기
    max_len = 0
    for value in dict_letter.values():
        if max_len == 0:
            max_len = value
        elif max_len < value:
            max_len = value

    print(f'#{tc} {max_len}')








