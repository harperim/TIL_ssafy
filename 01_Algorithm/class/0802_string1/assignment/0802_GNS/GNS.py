import sys
sys.stdin = open('GNS_input.txt')

T = int(input())

# 카운팅 정렬
# 0 1 2 3 4 5 6 7 8 9
# 0 0 2 0 0 1 0 0 5 2

for tc in range(1, T+1):

    dummy = input()  # 버리는 줄
    num_text = list(map(str, input().split()))

    result = []

    # 숫자 딕셔너리, 리스트 생성
    num_list = {
        'ZRO': 0,
        'ONE': 1,
        'TWO': 2,
        'THR': 3,
        'FOR': 4,
        'FIV': 5,
        'SIX': 6,
        'SVN': 7,
        'EGT': 8,
        'NIN': 9,
    }

    num_cnt = [0] * 10

    for text in num_text:               # 문자 1개씩 뽑아오기
        for key in num_list.keys():     # num_list의 key값 뽑아오기
            if text == key:             # 만약 일치한다면
                idx = num_list[key]     # idx 값을 숫자로 받아온 후
                num_cnt[idx] += 1       # +1 증가

    # num_list의 키 list로 반환
    keys = list(num_list.keys())

    # 결과를 저장할 리스트
    result = []

    for key, count in zip(keys, num_cnt):
        result.extend([key] * count)

    result = " ".join(result)
    print(f'#{tc} {result}')

