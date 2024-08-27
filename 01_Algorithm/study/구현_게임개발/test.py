"""
4 4         # 4 x 4 맵 생성
1 1 0       # (1, 1)에 북쪽(0)을 바라보고 서 있는 캐릭터
1 1 1 1     # 첫 줄은 모두 바다
1 0 0 1     # 둘째 줄은 바다/육지/육지/바다
1 1 0 1     # 셋째 줄은 바다/바다/육지/바다
1 1 1 1     # 넷째 줄은 모두 바다
"""

import sys
sys.stdin = open('input.txt', 'r')

row, column = list(map(int, input().split()))

direction = [0, 1, 2, 3]  # 북, 동, 남, 서

"""
# 빈 리스트 만들기 예시
a = [[0] * 4 for _ in range(4)]
print(a)

# 빈 리스트 생성 
empty = [[0]*row for _ in range(column)]
print(empty)
"""

# 현재 나의 위치/방향
x, y, direction = map(int, input().split())  # 1 1 0

# 현재 바다/육지 맵 리스트로 값 받아오기
map_li = []
for _ in range(row):
    sea_y = list(map(int, input().split()))
    map_li.append(sea_y)
print(map_li)  # [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]]

# 북, 동, 남, 서 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

"""
현재 나의 위치 (1, 1)

          북 (0, 1)
동 (1, 0)    (1, 1)   서 (1, 2)
          남 (2, 1)
"""

def turn_left():
    global direction
    direction -= 1  # 왼쪽으로 돌기
    if direction == -1:  # -1은 없으므로 3으로 다시 보내주기
        direction = 3


# 현재 나의 위치 찍기
# 내 방향 기준 왼쪽으로 방향 틀기
# 만약 그 방향에 가보지 않은 칸이 있다면 전진, 없다면 그대로 유지
# 다시 왼쪽 방향으로 돌기 반복
# 만약 네 방향 모두 1로 되어 있다면 방향 유치한채로 뒤로 한 칸
# 만약 뒤 칸도 1이라면 움직임 멈추기
# 첫째 줄에 이동을 마친 후 캐릭터가 방문한 칸의 수 출력

# 0 육지, 1 바다, 2 방문한 곳
count = 1  # 현재 내가 서 있는 지점부터 카운트 시작
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]  # 1 + 0 = 1
    ny = y + dy[direction]  # 1 + (-1) = 0
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동 
    if map_li[nx][ny] == 0:
        map_li[nx][ny] = 2  # 방문한 걸로 변경
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 1이거나(바다) 2인 경우(방문한 곳)
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if map_li[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

print(count)




