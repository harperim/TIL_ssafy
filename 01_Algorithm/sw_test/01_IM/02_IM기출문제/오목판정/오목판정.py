import sys
sys.stdin = open('오목판정_input.txt')


dx = [0, 1, 1, 1]
dy = [1, 1, 0, -1]

def func(N):
    for i in range(N):
        for j in range(N):
            for k in range(4):
                cnt = 0
                ni, nj = i, j
                # 현재 방향으로 이동하면서 돌이 연속되는지 확인
                while 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'o':
                    cnt += 1
                    if cnt == 5:
                        return 'YES'

                    ni += dx[k]
                    nj += dy[k]
    return 'NO'

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(N)]
    print(f'#{tc} {func(N)}')

