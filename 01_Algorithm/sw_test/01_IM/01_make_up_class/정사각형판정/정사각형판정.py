import sys
sys.stdin = open('정사각형판정_input.txt')

# 1. 가로 = 세로
# 2. 구역 내에서 #으로만 구성되어 있는지 판단


def find(arr):
    start = []
    total_cnt = cnt = 0
    for i in range(N):
        for j in range(N):
            # 시작 위치 구하기
            if arr[i][j] == '#' and len(start) == 0:
                start.extend([i, j])
            # 정사각형 길이 구하기
            if arr[i][j] == '#' and start[0] == i:
                cnt += 1
            # 전체 # 개수 구하기
            if arr[i][j] == '#':
                total_cnt += 1

    sx = start[0]
    sy = start[1]
    flag = 1
    for i in range(sx, sx+cnt):
        for j in range(sy, sy+cnt):
            # #이 아닌 경우
            if arr[i][j] != '#':
                flag = 0
        if flag == 0:
            break

    # 전체 #의 개수와 정사각형 #의 개수 같은지 확인
    if total_cnt != cnt * cnt:
        flag = 0

    if flag == 1:
        return 'yes'
    else:
        return 'no'


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(N)]

    answer = find(arr)
    print(f'#{tc} {answer}')


