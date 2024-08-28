import sys
sys.stdin = open('전봇대_input.txt')

T = int(input())

# 현재 내 위치보다 높이 있는 애가 있다면 +1
for tc in range(1, T+1):
    N = int(input())  # 전선 개수
    AB = [list(map(int, input().split())) for _ in range(N)]

    # AB.sort()  # 정렬 안 하면 fail

    cnt = 0  # 교차점 수
    for i in range(1, N):
        for j in range(i):  # 내 비보다 높은 곳에 설치된 곳이 있는지 확인 / A는 더 낮지만 B가 더 높은 경우 교차
            if AB[j][1] > AB[i][1]:
                cnt += 1
    print(f'#{tc} {cnt}')



