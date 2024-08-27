# 2056-연월일 달력

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
answer = ''

for i in range(1, T+1):
    answer += i[:3]
    if i[4:6] == '01':
        answer += '/' +i[4:6]
    if i[7:9] == '01':
        answer += '/'+i[7:9]
    else:
        print(-1)

    print(f'#{i} {answer}')
