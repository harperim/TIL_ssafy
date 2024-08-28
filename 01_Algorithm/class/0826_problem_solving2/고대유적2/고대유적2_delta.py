import sys
sys.stdin = open('고대유적2_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    picture = [list(map(int, input().split())) for _ in range(N)]
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    mx = 1
    for i in range(N):
        for j in range(M):
            if picture[i][j] == 1:
                cnt = 1
                for k in range(4):
                    ni, nj = i + di[k], j + dj[k]
                    if 0 <= ni < N and 0 <= nj < M:
                        cnt += 1
                        while True:
                            ni, nj = i + cnt * di[k], j + cnt * dj[k]
                            if 0 <= ni < N and 0 <= nj < M and picture[ni][nj] == 1:
                                if mx < cnt:
                                    mx = cnt
                                cnt += 1
                                continue
                            else:
                                break

    if mx == 1:
        print(f'#{tc} {0}')
    else:
        print(f'#{tc} {mx + 1}')
