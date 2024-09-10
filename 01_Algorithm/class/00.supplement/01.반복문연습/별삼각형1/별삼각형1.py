import sys
sys.stdin = open('별삼각형1_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    print(f'#{tc}')

    if M == 1:
        for i in range(1, N+1):
            print('*' * i)
    elif M == 2:
        for i in range(3, 0, -1):
            print('*' * i)
    # 중간줄 해당 개수
    elif M == 3:
        for i in range(1, N+1):
            print(' '*(N-i) + '*'*(i*2-1))


