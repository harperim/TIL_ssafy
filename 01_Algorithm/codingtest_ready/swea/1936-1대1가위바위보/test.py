# 1936-1대1 가위바위보

import sys
sys.stdin = open('input.txt', 'r')

A, B = map(int, input().split())
# print(A, B)

# A가 이기는 경우
if (A == 1 and B == 3) or (A == 2 and B == 1) or (A == 3 and B == 2):  # 가위1 바위2 보3
    print('A')
# B가 이기는 경우
else:
    print('B')

