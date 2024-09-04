import sys
sys.stdin = open('정사각형판정_input.txt')

# 1. 가로 = 세로
# 2. 구역 내에서 #으로만 구성되어 있는지 판단

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(N)]

