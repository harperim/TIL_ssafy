import sys;
sys.stdin = open('풍선팡_input.txt')

T = int(input())
# 네 방향 탐색을 위한 배열
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 최대 꽃가루 수를 저장할 변수
    max_confetti = 0

    # 2차 배열 순회
    for i in range(N):
        for j in range(M):
            # 현재 위치의 꽃가루 수
            current_confetti = arr[i][j]
            for h in range(1,  arr[i][j]+1): #확장 범위 설정
                # 네 방향 탐색
                for k in range(4):
                    ni = i + di[k] * h
                    nj = j + dj[k] * h

                    # 인덱스 체크
                    if 0 <= ni < N and 0 <= nj < M:
                        current_confetti += arr[ni][nj]

            # 최대 꽃가루 수 갱신
            if current_confetti > max_confetti:
                max_confetti = current_confetti

    # 결과 출력
    print(f'#{tc} {max_confetti}')
