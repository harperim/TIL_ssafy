# 2072-홀수만 더하기

import sys
sys.stdin = open('input.txt', 'r')


T = int(input())

for tc in range(1, T+1):
    li = map(int, input().split())
    answer = 0
    for i in li:
        # print(i)
        if i % 2 != 0:
            answer += i
    print(f'#{tc} {answer}')

