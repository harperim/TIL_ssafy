import sys
sys.stdin = open('연산자끼워넣기_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    symbols_cnt = list(map(int, input().split()))

    # 순열은 시간초과남, 백트레킹으로 접근해보기
    for i in range(len(symbols_cnt)):
        pass

