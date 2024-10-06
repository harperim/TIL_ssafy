from collections import deque

NICKNAME = "기본코드"
map_data = []  # 맵 정보
allies = {}  # 아군 정보
enemies = {}  # 적군 정보
codes = []  # 암호문 정보

class Bridge:
    def init(self, nickname):
        # 닉네임을 사용하여 초기화 (서버에서 게임 데이터를 받아오는 것 가정)
        return "game data"  # 예시로 임의의 게임 데이터를 반환합니다.

    def submit(self, output):
        # 명령어를 서버로 전송하여 다음 게임 데이터를 받아옴
        return "next game data"  # 예시로 임의의 다음 게임 데이터를 반환합니다.

    def close(self):
        # 서버 연결을 종료합니다.
        pass

def main():
    bridge = Bridge()
    game_data = bridge.init(NICKNAME)

    while len(game_data) > 0:
        parse_data(game_data)

        # 현재 탱크 위치 파악
        my_position = find_my_position()
        target_position = find_target_position()

        # 최단 경로 계산
        path = find_shortest_path(my_position, target_position)

        # 이동 및 공격 명령어 설정
        output = get_next_action(my_position, target_position, path)

        # 명령어 전송
        game_data = bridge.submit(output)

    bridge.close()

# 명령어 설정 함수
def get_next_action(my_position, target_position, path):
    if path:
        return f"{path.pop(0)} A"  # 다음 방향으로 이동
    elif is_adjacent(my_position, target_position):
        return f"{get_direction_to_face_x(my_position, target_position)} F M"  # 공격 명령
    else:
        return "S"  # 대기

# BFS로 최단 경로 찾기
def find_shortest_path(start, target):
    queue = deque([start])
    visited = [[False] * len(map_data[0]) for _ in range(len(map_data))]
    direction_map = {}

    visited[start[0]][start[1]] = True

    while queue:
        current = queue.popleft()
        current_pos = f"{current[0]},{current[1]}"

        if current == target:
            return reconstruct_path(current_pos, direction_map, start)

        explore_neighbor(queue, visited, current[0] - 1, current[1], current_pos, direction_map, "U")
        explore_neighbor(queue, visited, current[0] + 1, current[1], current_pos, direction_map, "D")
        explore_neighbor(queue, visited, current[0], current[1] - 1, current_pos, direction_map, "L")
        explore_neighbor(queue, visited, current[0], current[1] + 1, current_pos, direction_map, "R")

    return []  # 경로가 없을 경우 빈 리스트 반환

# 이웃 탐색 함수
def explore_neighbor(queue, visited, new_row, new_col, current_pos, direction_map, direction):
    if can_move_to(new_row, new_col) and not visited[new_row][new_col]:
        visited[new_row][new_col] = True
        queue.append([new_row, new_col])
        direction_map[f"{new_row},{new_col}"] = f"{direction},{current_pos}"

# 경로 복원 함수
def reconstruct_path(target, direction_map, start):
    path = []
    current = target

    start_pos = f"{start[0]},{start[1]}"

    while current != start_pos:
        data = direction_map[current].split(",")
        path.append(data[0])
        current = data[1]

    path.reverse()  # 경로를 역순으로
    return path

# 탱크의 현재 위치를 찾는 함수
def find_my_position():
    for i in range(len(map_data)):
        for j in range(len(map_data[i])):
            if map_data[i][j] == "A":
                return [i, j]
    return None

# 적군 포탑 X의 위치를 찾는 함수
def find_target_position():
    for i in range(len(map_data)):
        for j in range(len(map_data[i])):
            if map_data[i][j] == "X":
                return [i, j]
    return None

# 특정 좌표로 이동할 수 있는지 확인하는 함수
def can_move_to(row, col):
    return 0 <= row < len(map_data) and 0 <= col < len(map_data[0]) and map_data[row][col] == "G"

# 두 좌표가 인접한지 확인하는 함수
def is_adjacent(current, target):
    row_diff = abs(current[0] - target[0])
    col_diff = abs(current[1] - target[1])
    return (row_diff == 1 and col_diff == 0) or (row_diff == 0 and col_diff == 1)

# X를 향해 방향을 맞추는 함수
def get_direction_to_face_x(my_position, target_position):
    my_row, my_col = my_position
    target_row, target_col = target_position

    if my_row > target_row:
        return "U"  # X가 위쪽에 있으면 위쪽으로 바라보기
    elif my_row < target_row:
        return "D"  # X가 아래쪽에 있으면 아래쪽으로 바라보기
    elif my_col > target_col:
        return "L"  # X가 왼쪽에 있으면 왼쪽으로 바라보기
    else:
        return "R"  # X가 오른쪽에 있으면 오른쪽으로 바라보기

# 입력 데이터를 파싱하여 변수에 저장
def parse_data(game_data):
    global map_data, allies, enemies, codes

    rows = game_data.split("\n")
    row_index = 0

    # 첫 번째 행 데이터 읽기
    header = rows[row_index].split(" ")
    map_height = int(header[0])
    map_width = int(header[1])
    num_of_allies = int(header[2])
    num_of_enemies = int(header[3])
    num_of_codes = int(header[4])
    row_index += 1

    # 맵 정보를 초기화하고 다시 읽어오기
    map_data = [rows[row_index + i].split(" ") for i in range(map_height)]
    row_index += map_height

    # 아군 정보를 초기화하고 다시 읽어오기
    allies = {}
    for i in range(num_of_allies):
        ally_data = rows[row_index + i].split(" ")
        ally_name = ally_data[0]
        ally_info = ally_data[1:]
        allies[ally_name] = ally_info
    row_index += num_of_allies

    # 적군 정보를 초기화하고 다시 읽어오기
    enemies = {}
    for i in range(num_of_enemies):
        enemy_data = rows[row_index + i].split(" ")
        enemy_name = enemy_data[0]
        enemy_info = enemy_data[1:]
        enemies[enemy_name] = enemy_info
    row_index += num_of_enemies

    # 암호문 정보를 초기화하고 다시 읽어오기
    codes = [rows[row_index + i] for i in range(num_of_codes)]