# 2070-큰 놈, 작은 놈, 같은 놈

import sys
sys.stdin = open('input.txt', 'r')
#
T = int(input())

for tc in range(1, T+1):
    li = list(map(int, input().split()))
    # print(li)
    if li[0] < li[1]:
        answer = "<"
    elif li[0] == li[1]:
        answer = "="
    else:
        answer = ">"

    print(f'#{tc} {answer}')

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     li = map(int, input())
#     print(li)
