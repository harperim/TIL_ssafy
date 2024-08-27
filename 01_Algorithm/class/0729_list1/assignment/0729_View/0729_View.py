import sys
sys.stdin = open('View_input.txt', 'r')

T = 10

for tc in range(1, T+1):
    n = int(input())  # 10
    arr = list(map(int, input().split()))
    result = 0

    for i in range(2, n-2):
        max_v = 0          # i-2, i-1, i+1, i+2 중에 최대값
        for j in range(5):  # [-2, -1, 1, 2]
            if j != 2:  # 자기 자신은 제외
                if max_v < arr[i-2+j]:  # i-2가 시작 위치
                    max_v = arr[i-2+j]

        # 좌우 2개 최대값하고 기준값 비교해서 조망권 누적
        if arr[i] > max_v:
            result += arr[i] - max_v
    print(f'#{tc} {result}')
