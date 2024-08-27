import sys
sys.stdin = open('진기의최고급붕어빵_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))

    # 붕어빵 1개 만들 때 걸리는 시간
    time = K / M

    # 현재 붕어빵 개수
    c_cnt = 0

    # while 오기로 한 사람한테 붕어빵 다 나눠주면
    for i in range(N):
        if arr[i] == 0:
            pass




