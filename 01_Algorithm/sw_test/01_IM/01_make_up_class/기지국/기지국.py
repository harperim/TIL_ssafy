import sys
sys.stdin = open('기지국_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(N)]
    row = N // 2  # 4

