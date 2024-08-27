# 2058-자릿수더하기

import sys
sys.stdin = open('input.txt', 'r')

num = input()
answer = 0
for i in num:
    answer += int(i)
print(answer)
