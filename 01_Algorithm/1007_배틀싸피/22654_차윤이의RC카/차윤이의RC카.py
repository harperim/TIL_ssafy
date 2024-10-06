import sys
sys.stdin = open('차윤이의RC카_input.txt')

# RC카의 각 방향에 따른 이동 좌표 변화 (상, 우, 하, 좌)
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def simulate_rc_car(N, field, commands, start, end):
    x, y = start  # RC카의 현재 위치
    direction = 0  # 시작 방향 (0: 위쪽)

    for command in commands:
        if command == 'A':
            # 현재 방향으로 이동 시도
            dx, dy = directions[direction]
            nx, ny = x + dx, y + dy
            # 이동 가능한 땅(G)인 경우에만 이동
            if 0 <= nx < N and 0 <= ny < N and field[nx][ny] != 'T':
                x, y = nx, ny
        elif command == 'L':
            # 왼쪽으로 90도 회전
            direction = (direction - 1) % 4
        elif command == 'R':
            # 오른쪽으로 90도 회전
            direction = (direction + 1) % 4

    # 최종 위치가 목적지인지 확인
    return (x, y) == end


def main():
    T = int(input().strip())  # 테스트 케이스 수

    for t in range(1, T + 1):
        N = int(input().strip())
        field = [input().strip() for _ in range(N)]
        Q = int(input().strip())

        # 시작 위치(X)와 목적지(Y) 위치 찾기
        start = end = None
        for i in range(N):
            for j in range(N):
                if field[i][j] == 'X':
                    start = (i, j)
                elif field[i][j] == 'Y':
                    end = (i, j)

        case_result = []

        for _ in range(Q):
            command_data = input().strip().split()
            C = int(command_data[0])
            commands = command_data[1]
            # RC카가 목적지에 도달할 수 있는지 확인
            if simulate_rc_car(N, field, commands, start, end):
                case_result.append("1")
            else:
                case_result.append("0")

        # 테스트 케이스 결과 출력
        print(f"#{t} " + " ".join(case_result))


# 실행
main()


