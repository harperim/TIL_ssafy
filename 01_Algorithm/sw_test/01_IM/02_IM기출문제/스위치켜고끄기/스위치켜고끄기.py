import sys;
sys.stdin = open('스위치켜고끄기_input.txt')


def change(num):
    """스위치 상태를 토글하는 함수.
    스위치가 꺼져 있으면 켜고, 켜져 있으면 꺼지게 한다."""
    if switch[num] == 0:
        switch[num] = 1
    else:
        switch[num] = 0
    return


# 스위치의 개수 입력
N = int(input())

# 스위치의 초기 상태 입력 (0은 꺼져 있는 상태, 1은 켜져 있는 상태)
# 스위치 인덱스를 1부터 시작하기 위해, 인덱스 0에는 -1을 설정
switch = [-1] + list(map(int, input().split()))

# 학생의 수 입력
students = int(input())

# 각 학생의 성별과 받은 수에 따라 스위치 상태를 조작
for _ in range(students):
    sex, num = map(int, input().split())

    # 남학생: 받은 수의 배수에 해당하는 모든 스위치의 상태를 토글
    if sex == 1:
        #배수 찾아주는 코드
        for i in range(num, N + 1, num):
            change(i)  # 위에 토글 i번째 스위치를 바꾼다

    # 여학생: 받은 수를 중심으로 좌우 대칭을 검사하여 가장 큰 구간의 스위치 상태를 토글
    else:
        # 중심 스위치의 상태를 토글
        change(num)

        # 인덱스 구간 안에 있는지 확인
        for k in range(1, N // 2 + 1):
            # 좌측과 우측의 인덱스가 범위를 벗어나면 종료
            # num + k 오른 쪽,  num - k 왼쪽
            if num + k > N or num - k < 1:
                break

            # 좌측과 우측 스위치의 상태가 같으면 구간 확장
            # 스위치 같은지 확인
            if switch[num + k] == switch[num - k]:
                change(num + k)
                change(num - k)
            else:
                # 상태가 다르면 구간 확장 종료
                break

# 최종 스위치 상태를 20개씩 출력
for i in range(1, N + 1):
    print(switch[i], end=" ")
    if i % 20 == 0:
        print()  # 20개 출력 후 줄 바꿈
