import sys
sys.stdin = open('최소합_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    path = []  # 경로를 기록할 리스트
    used = [0] * N  # 1~7 숫자의 사용 여부를 기록할 리스트

