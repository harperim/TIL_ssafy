import sys
sys.stdin = open('전구와스위치_input.txt')

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     lamp = [list(map(int, input())) for _ in range(2)]
#
#     start = lamp[0]
#     end = lamp[1]
#
#     while start != end:
#         cnt = 0
#         for i in range(N):
#             if start[i] == end[i]:
#                 continue
#             else:
#                 if i == 0:
#                     start[i] = (start[i] + 1) % 2
#                     start[i + 1] = (start[i + 1] + 1) % 2
#                     cnt += 1
#                 elif i == N:
#                     start[i - 1] = (start[i - 1] + 1) % 2
#                     start[i] = (start[i] + 1) % 2
#                     cnt += 1
#                 else:
#                     start[i-1] = (start[i-1] + 1) % 2
#                     start[i] = (start[i] + 1) % 2
#                     start[i+1] = (start[i+1] + 1) % 2
#                     cnt += 1
#     print(f'#{tc} {cnt}')

# ----------------------------
# 다른 사람 풀이
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    Ai = list(map(int, input()))
    Bi = list(map(int, input()))

    # Ai[0]을 눌렀을 때
    lst = []
    for i in range(N):
        lst.append(Ai[i])

    lst[0] = 1 - lst[0]
    lst[1] = 1 - lst[1]
    cnt = 1

    for i in range(1, N):
        if lst[i - 1] != Bi[i - 1]:
            if i + 1 < N:
                lst[i] = 1 - lst[i]
                lst[i - 1] = 1 - lst[i - 1]
                lst[i + 1] = 1 - lst[i + 1]
                cnt += 1

            elif i == N - 1:
                lst[i] = 1 - lst[i]
                lst[i - 1] = 1 - lst[i - 1]
                cnt += 1

    if lst != Bi:
        cnt = -1

    # Ai[0]을 누르지 않았을 때
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

    if lst1 != Bi:
        cnt1 = -1

    if cnt == -1 and cnt1 == -1:
        cnt = -1
    elif cnt == -1:
        cnt = cnt1
    elif cnt1 == -1:
        cnt = cnt
    else:
        if cnt > cnt1:
            cnt = cnt1

    print(f'#{tc} {cnt}')
