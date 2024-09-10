import sys
sys.stdin = open('전구와스위치_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    Ai = list(map(int, input()))
    Bi = list(map(int, input()))

    # 2가지 경우의 수로 나누어서 시작
    # 1. Ai[0]을 눌렀을 때 : 0번째 idx 먼저 누르고 시작
    lst = []
    for i in range(N):
        lst.append(Ai[i])

    lst[0] = 1 - lst[0]
    lst[1] = 1 - lst[1]
    cnt = 1

    for i in range(1, N):
        if lst[i - 1] != Bi[i - 1]:
            if i + 1 < N:           # 중간에 위치했다면
                lst[i] = 1 - lst[i]
                lst[i - 1] = 1 - lst[i - 1]
                lst[i + 1] = 1 - lst[i + 1]
                cnt += 1

            elif i == N - 1:        # 맨 마지막에 위치했다면
                lst[i] = 1 - lst[i]
                lst[i - 1] = 1 - lst[i - 1]
                cnt += 1

    if lst != Bi:
        cnt = -1

    # 2. Ai[0]을 누르지 않았을 때 : 0번째 인덱스를 누르지 않은 경우
    lst1 = []
    for i in range(N):
        lst1.append(Ai[i])
    cnt1 = 0

    for i in range(1, N):
        if lst1[i - 1] != Bi[i - 1]:
            if i + 1 < N:
                lst1[i] = 1 - lst1[i]
                lst1[i - 1] = 1 - lst1[i - 1]
                lst1[i + 1] = 1 - lst1[i + 1]
                cnt1 += 1

            elif i == N - 1:
                lst1[i] = 1 - lst1[i]
                lst1[i - 1] = 1 - lst1[i - 1]
                cnt1 += 1

    # 판별하기
    if lst1 != Bi:  # 바꾼 결과와 기댓값이 다르면
        cnt1 = -1

    if cnt == -1 and cnt1 == -1:  # 두 값 모두 -1이면
        cnt = -1
    elif cnt == -1:  # cnt == -1이면 cnt1을 출력
        cnt = cnt1
    elif cnt1 == -1:  # cnt1 == -1이면 cnt를 출력
        cnt = cnt
    else:               # 둘 다 값을 가지고 있다면 더 좋은 성능의 값을 출력
        if cnt > cnt1:
            cnt = cnt1

    print(f'#{tc} {cnt}')


