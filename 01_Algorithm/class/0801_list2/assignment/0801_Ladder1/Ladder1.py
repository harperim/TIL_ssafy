import sys
sys.stdin = open('Ladder1_input.txt')

# 내가 풀던 풀이
# T = 10
# n = int(input())
#
# # 좌, 우, 상
# dx = [0, 0, -1]
# dy = [-1, 1, 0]
#
# # 좌우 >> 상 : 아래에서 위로 올라가는데, 올라가는 것보다 좌우가 우선
# for tc in range(1, T+1):
#     arr = [list(map(int, input().split())) for _ in range(100)]
#     finish = []
#
#     # 도착점 찾기
#     finish.append(-1)
#     for j in range(100):
#         if arr[-1][j] == 2:
#             finish.append(j)
#     print(finish)
#
#
#     # 1이라면 좌우상으로 움직이기
#     # 지나온 곳은 0으로 값 변경
#
#     # i == 0이 되면 종료

# 해설
def find_start(arr):
    for i in range(n):
        if arr[n-1][i] == 2:
            x = n-1
            y = i
            return x, y

def ladder(arr, x, y):
    while True:
        # 만약 x좌표가 0일 때, y좌표를 리턴
        if x == 0:
            return y
        else:
            for i in range(3):
                nx = x + dx[i]
                ny = y + dy[i]
                # 인덱스 체크 먼저, 벽 체크
                if 0 <= nx < n and 0 <= ny < n:
                    if arr[nx][ny] == 1:
                        x, y = nx, ny  # 현재 좌표를 갱신
                        arr[x][y] = 9  # 0으로 대입해도 됨
                        break

T = 10
n = 100

dx = [0, 0, -1]  # 왼, 오, 위
dy = [-1, 1, 0]

for tc in range(1, T+1):
    dummy = input()
    arr = [list(map(int, input().split())) for _ in range(100)]
    x, y = find_start(arr)  # 출발점 세팅 (x, y)

    ans = ladder(arr, x, y)
    print(f'#{tc} {ans}')


