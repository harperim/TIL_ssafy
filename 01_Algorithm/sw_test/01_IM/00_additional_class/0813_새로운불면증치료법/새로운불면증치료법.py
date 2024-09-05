import sys
sys.stdin = open('새로운불면증치료법_input.txt')

T = int(input())

for tc in range(1, T):
    N = int(input())
    num = set()
    x = 1
    while len(num) < 10:
        num |= set(str(x*N))
        x += 1
    print(f'#{tc} {(x-1)*N}')




