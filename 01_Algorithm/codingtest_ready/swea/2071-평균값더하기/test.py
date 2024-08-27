# 2071-평균값 더하기

import sys
sys.stdin = open('input.txt', 'r')


T = int(input())

for tc in range(1, T+1):
    li = map(int, input().split())
    answer = 0
    length = 0
    for i in li:
        # print(i)
        answer += i
        length += 1
    answer = round(answer / length)
    print(f'#{tc} {answer}')
