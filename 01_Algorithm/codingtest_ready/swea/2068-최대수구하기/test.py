import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for i in range(1, T+1):
    num = list(map(int, input().split()))
    answer = max(num)
    print(f'#{i} {answer}')
