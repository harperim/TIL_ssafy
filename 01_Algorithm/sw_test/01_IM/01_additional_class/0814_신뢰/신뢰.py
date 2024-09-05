import sys
sys.stdin = open('신뢰_input.txt')

T = int(input())

# 표시된 순서대로 버튼을 눌러야 함
# 동시에 버튼을 못 누른다 = 같은 버튼을 눌러도 무방함
for tc in range(1, T+1):
    btn = input().split()

    o_pos = 1       # 오렌지 로봇의 시작 위치
    b_pos = 1       # 블루 로봇의 시작 위치
    o_time = 0      # 오렌지 로봇이 이전 작업을 끝낸 시간
    b_time = 0      # 블루 로봇이 이전 작업을 끝낸 시간
    N = int(btn[0])  # 로봇의 작업 횟수

    # btn에서 홀수 인덱스 = 로봇 구분, 짝수 인덱스 = 스위치 번호
    # N번 반복, 2개씩 끊어서 봐야하므로 1/3/5/7/9 인덱스일 때 자르기
    for i in range(1, 2*N, 2):       # i 로봇의 인덱스
        robot = btn[i]  # btn[i] : 이번에 작업할 로봇, btn[i+1] 누를 스위치 번호
        switch = int(btn[i+1])      # 정수형 스위치 번호
        if robot == 'O':        # 오렌지 로봇인 경우
            # 오렌지 로봇이 이번 스위치를 누르는 시간
            tmp = o_time + abs(o_pos - switch) + 1      # 이전 작업 완료 시간 + 소요 시간(이동 시간 + 1초)
            if tmp <= b_time:       # blue의 작업이 더 늦게 끝나면
                tmp = b_time + 1    # 순서를 지켜야 한다. / blue가 끝난 시간보다 늦게 끝나야 함
            o_time = tmp        # 스위치를 누른 시간 확정
            o_pos = switch
        else:       # 블루 로봇인 경우
            # 블루 로봇이 이번 스위치를 누르는 시간
            tmp = b_time + abs(b_pos - switch) + 1  # 이전 작업 완료 시간 + 소요 시간(이동 시간 + 1초)
            if tmp <= o_time:  # blue의 작업이 더 늦게 끝나면
                tmp = o_time + 1  # 순서를 지켜야 한다. / blue가 끝난 시간보다 늦게 끝나야 함
            b_time = tmp  # 스위치를 누른 시간 확정
            b_pos = switch

    print(f'#{tc} {max(o_time, b_time)}')
