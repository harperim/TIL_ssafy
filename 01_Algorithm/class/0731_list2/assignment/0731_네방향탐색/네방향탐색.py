import sys
sys.stdin = open('네방향탐색_input.txt')

T = int(input())

# 우, 하, 좌, 상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


for tc in range(1, T+1):

    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    total = 0
    for i in range(n):
        for j in range(n):  # NxN 배열의 모든 원소에 대해 => 라는 문장이 있으면 for문 일단 2개 쓰기
            sum_val = 0  # 원소와 인접원소 차 절댓값의 합
            # i, j 원소의 4 방향
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                # 인덱스 체크 (방문 체크, 조건 등등...)
                if 0 <= ni < n and 0 <= nj < n:
                    # abs 쓰지 않기 위해 if문으로 나누기
                    if arr[i][j] - arr[ni][nj] > 0:
                        total += arr[i][j] - arr[ni][nj]  # 실존하는 인접원소 ni, nj
                    else:
                        total += arr[ni][nj] - arr[i][j]

    print(f'#{tc} {total}')  # 2430



