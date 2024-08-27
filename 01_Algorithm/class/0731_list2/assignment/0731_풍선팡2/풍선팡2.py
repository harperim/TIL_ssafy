import sys
sys.stdin = open('풍선팡2_input.txt')

T = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for tc in range(1, T+1):
    row, column = map(int, input().split())  # 3 5
    balloon = [list(map(int, input().split())) for _ in range(row)]

    # 꽃가루 최대값
    max_sum = 0

    for i in range(row):  # 0 1 2
        for j in range(column):  # 0 1 2 3 4

            sum_val = 0
            # 자기 자신 더하기
            sum_val += balloon[i][j]

            for k in range(4):
                # 새로운 방향에 좌표 설정
                nx = i + dx[k]
                ny = j + dy[k]

                # 인덱스 체크
                if 0 <= nx < row and 0 <= ny < column:
                    sum_val += balloon[nx][ny]
            if sum_val > max_sum:
                max_sum = sum_val
    print(f'#{tc} {max_sum}')

