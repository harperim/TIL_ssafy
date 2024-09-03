import sys
sys.stdin = open('러시아국기같은깃발_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(N)]

