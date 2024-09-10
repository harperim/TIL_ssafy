import sys
sys.stdin = open('사냥꾼_input.txt')

T = int(input())
dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for i in range(N):
        for j in range(N):
            # 사냥꾼인 경우
            if arr[i][j] == 1:
                for k in range(8):  # 방향 탐색
                    for l in range(1, N):  # 길이 설정
                        nx = i + dx[k] * l
                        ny = j + dy[k] * l
                        if 0 <= nx < N and 0 <= ny < N:
                            # 돌 만나면 멈추기
                            if arr[nx][ny] == 3:
                                break
                            # 토끼 만나면 cnt += 1
                            if arr[nx][ny] == 2:
                                cnt += 1

    print(f'#{tc} {cnt}')

