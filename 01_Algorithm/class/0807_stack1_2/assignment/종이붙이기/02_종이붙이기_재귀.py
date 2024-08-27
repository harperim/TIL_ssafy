import sys
sys.stdin = open('종이붙이기_input.txt')

def f(n):
    if n <= 1:
        return 1
    else:
        return f(n-1) + 2*f(n-2)

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 10의 배수
    print(f'#{tc} {f(N//10)}')
