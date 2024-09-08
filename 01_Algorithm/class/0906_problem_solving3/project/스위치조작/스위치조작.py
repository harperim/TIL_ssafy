import sys
sys.stdin = open('스위치조작_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    switch = [list(map(int, input().split())) for _ in range(2)]
    start = switch[0]
    end = switch[1]

    while start != end:
        cnt = 0
        for i in range(N):
            if start[i] == end[i]:
                continue
            for j in range(i, N):
                if start[j] == 0:
                    start[j] = 1
                else:
                    start[j] = 0
            cnt += 1
    print(f'#{tc} {cnt}')


