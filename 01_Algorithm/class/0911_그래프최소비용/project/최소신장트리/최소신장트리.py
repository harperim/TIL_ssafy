import sys
sys.stdin = open('최소신장트리_input.txt')

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]

