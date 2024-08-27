import sys
sys.stdin = open("중력_input.txt", 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_val = 0
    for i in range(N):  # 7 4 2 0 0 6 0 7 0
        cnt = 0
        for j in range(i+1, N):
            if arr[i] > arr[j]:
                cnt += 1

        if max_val < cnt:
            max_val = cnt
    print(f'#{tc} {max_val}')



