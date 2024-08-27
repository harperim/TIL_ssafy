import sys
sys.stdin = open('간단한369게임_input.txt')

"""
1. 1~N까지 in num 만들기
2. num의 각 자릿수 알아내기
3. 3, 6, 9에 해당하는 개수
"""

# 시험에서 sum, count 사용 가능
# diff 사이트 - 내가 출력한 값 넣어서 결과 확인 가능

# print(i, end=' ')  # 끝에 빈 칸 넣는 기법


# 1. 강사님 풀이
# N = int(input())

# 1 -> N까지 들어있는 리스트 만들기
# arr = [i for i in range(1, N+1)]
# arr = list(range(1, N+1))

# 369가 들어있는지 검사
# 1 -> N 만들기
# for x in arr:
#     c = ''
#     xx = x      # 복사본
#     while xx > 0:
#         d = xx % 10      # 1의 자리
#         if d > 0 and d % 3 == 0:    # 3, 6, 9인 경우
#             c += '-'
#         xx //= 10     # 10으로 나눈 후 1의 자리 버리기
#     if c == '':
#         print(x, end=' ')
#     else:
#         print(c, end=' ')

# 실행시간 : 무한루프에만 빠지지 않으면 됨 (1문제)
# 제출할 때마다 pass/fail 나오고 제출 횟수 제한 없음
# 문제마다 제출 횟수 제한 다르므로 잘 확인하기
# A형 : 불필요한 코드면 안됨 (2중 for문으로 해결되는 문제 3중 for문으로 한다면 시간초과)

# 2. 다른 분 풀이
# N = int(input())
# numbers = []
# for num in range(1, N + 1):
#     if num < 10:
#         if str(num) in '369':
#             num = '-'
#             numbers.append(num)
#         else:
#             numbers.append(num)
#     elif num >= 10:
#         cnt = 0
#         for j in str(num):
#             if str(j) in '369':
#                 cnt += 1
#         if cnt > 0:
#             numbers.append('-' * cnt)
#         else:
#             numbers.append(num)
#
# print(*numbers)


# 3. 내 풀이
N = int(input())
answer = ''

for num in range(1, N+1):

    # 숫자 안에 369 몇 개 있는지 개수 세기
    cnt = 0
    for n in str(num):
        if n in '369':
            cnt += 1

    # 369가 없으면 숫자 추가
    if cnt == 0:
        answer += str(num) + ' '
    # 1개라도 있으면 - 반환 (# '-' * 개수)/
    else:
        answer += '-'*cnt + ' '

print(answer)




