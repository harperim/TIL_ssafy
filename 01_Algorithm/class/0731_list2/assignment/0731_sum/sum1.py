import sys
sys.stdin = open('sum_input.txt')

T = 10

max_v = 0
for tc in range(1, T+1):
    dummy = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_v = 0
    # 행 우선 (행의 합)
    for i in range(100):
        sum_v = 0  # 행의 합이므로 여기에 위치
        for j in range(100):
            sum_v += arr[i][j]
        # 최대값
        if max_v < sum_v:
            max_v = sum_v

    # 열 우선 (열의 합)
    for i in range(100):
        sum_v = 0  # 행의 합이므로 여기에 위치
        for j in range(100):
            sum_v += arr[j][i]
        # 최대값
        if max_v < sum_v:
            max_v = sum_v

    # \ : 0, 0부터 시작하는 대각선합 구하기
    sum_v = 0
    for i in range(100):
        sum_v += arr[i][i]
    if max_v < sum_v:
        max_v = sum_v

    # / : -1, 0부터 시작하는 대각선합 구하기
    sum_v = 0
    for i in range(100):
        sum_v += arr[i][100-1-i]
    if max_v < sum_v:
        max_v = sum_v

    print(f'#{tc} {max_v}')
