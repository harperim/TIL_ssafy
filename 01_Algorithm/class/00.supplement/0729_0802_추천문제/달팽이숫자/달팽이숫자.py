import sys
sys.stdin = open('달팽이숫자_input.txt')

T = int(input())

direction = [0, 1, 2, 3]  # 동, 남, 서, 북
d_idx = 0  # 방향 인덱스

# 동, 남, 서, 북 방향
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
# 문자사각형


# 방향 전환 함수 생성
def turn_direction():
    global d_idx
    d_idx += 1  # 동, 남, 서, 북으로 방향 옮겨가기
    if d_idx == 4:  # 만약 idx=4라면, 해당 값은 없으므로
        d_idx = 0   # 0으로 재설정


for tc in range(1, T+1):
    n = int(input())+1  # 행렬 길이

    # 번호판 생성
    result = [[0] * n for _ in range(n)]
    number = 1  # 번호판에 넣을 번호

    for i in range(n):
        for j in range(n):
            if 0 <= i < n and 0 <= j < n:  # 행렬 번호판 범위에 해당되면
                result[i][j] = number
                number += 1
            else:
                turn_direction()


    # 방향은 동남서북으로 설정
    # 만약 범위를 벗어나는 경우라면 90도 방향으로 변환 (idx += 1)
    # 만약 direction == 4인 경우, 0으로 재설정




