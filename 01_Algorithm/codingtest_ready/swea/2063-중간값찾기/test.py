# 2063-중간값 찾기

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
num = list(map(int, input().split()))
num.sort()

answer = num[T//2]
print(answer)
