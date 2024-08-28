import sys
sys.stdin = open('고대유적2_input.txt')

T = int(input())

# 연속한 1의 개수 셀 줄 알아야 함
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0  # 가장 긴 구조물 길이

    # 행 순회
    for i in range(N):  # 가로 구조물 확인
        cnt = 0         # 구조물 길이
        for j in range(M):  # 세로 구조물 확인
            if arr[i][j]:  # 구조물이면
                cnt += 1
                if max_v < cnt:  # 구조물의 최대 길이 찾기
                    max_v = cnt
            else:  # 구조물이 아닌 경우
                cnt = 0

    # 열 순회
    for j in range(M):
        cnt = 0     # 열별로 cnt 초기화
        for i in range(N):
            if arr[i][j]:  # 구조물이면
                cnt += 1
                if max_v < cnt:
                    max_v = cnt
            else:  # 구조물이 아닌 경우
                cnt = 0

    # 노이즈만 있는 경우
    if max_v < 2:
        max_v = 0

    print(f'#{tc} {max_v}')
