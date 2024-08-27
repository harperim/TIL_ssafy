import sys
sys.stdin = open('숫자카드_input.txt')
# sys.stdout = open('숫자카드_output.txt', 'w')


# T = int(input())
#
# for tc in range(1, T+1):
#     n = int(input())
#     num_li = list(map(int, input()))
#
#     counts = {}
#
#     # 딕셔너리로 숫자:개수 저장하기
#     for num in num_li:
#         if num not in counts:
#             counts[num] = 1
#         else:
#             counts[num] += 1
#
#     # max_key 값 찾기 : 카드 장수가 같은 경우, 큰 숫자가 출력되어야 하므로
#     max_key = list(counts.keys())[0]
#     for key in counts.keys():
#         if key > max_key:
#             max_key = key
#
#     # max_val 값 찾기
#     max_val = counts[max_key]
#
#     for key, value in counts.items():
#         if value > max_val:
#             max_key = key
#             max_val = value
#
#     print(f'#{tc} {max_key} {max_val}')

# 강사님 풀이

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))  # 숫자가 각각 받을 때는 splite() 생략

    # 카운팅
    cnts = [0] * 10
    for i in range(N):
        cnts[arr[i]] += 1

    # 최대값의 인덱스
    max_i = 0
    for i in range(1, 10):
        if cnts[max_i] <= cnts[i]:
            max_i = i

    # 출력
    print(f'#{tc} {max_i} {cnts[max_i]}')
