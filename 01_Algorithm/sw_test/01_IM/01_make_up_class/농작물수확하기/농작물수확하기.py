import sys
sys.stdin = open('농작물수확하기_input.txt')

T = int(input())  # T: 1
for tc in range(1, T + 1):  # tc: 1
    N = int(input())        # N: 5
    arr = [list(map(int, input())) for _ in range(N)]  # arr: [[1,4,0,5,4],[4,4,2,5,0],[0,2,0,3,2],[5,1,2,0,4],[5,2,2,1,2]]

    total_sum = 0
    center = N // 2  # 중앙 인덱스 찾기  center: 2 -> 5//2  마름모 모양의 수확 범위를 계산하기 위해서 해줌

    for i in range(N): #행
        # 절댓값을 수동으로 구함
        if center > i:   #i: 0   # i가 중앙보다 위쪽에 있는지, 아래쪽에 있는지를 판단
            start = center - i # start: 2  좌측으로 얼마나 멀리 떨어져 있는지를 계산
        else:
            start = i - center

        end = N - start      #end : 3 ->  5 -2  우측으로 어디까지 수확할 수 있는지 계산
        row_sum = 0
        for j in range(start, end):  # 열  j: 2
            total_sum += arr[i][j]  # i번째 행에서 start 열부터 end 열까지의 값을 더하는 역할

    print(f'#{tc} {total_sum}')

