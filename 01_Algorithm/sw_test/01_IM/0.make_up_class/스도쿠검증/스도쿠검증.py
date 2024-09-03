import sys
sys.stdin = open('스도쿠검증_input.txt')

T = int(input())

for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(10)]

