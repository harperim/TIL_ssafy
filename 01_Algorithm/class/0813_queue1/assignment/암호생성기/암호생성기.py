import sys
sys.stdin = open('암호생성기_input.txt')

# T = 10
#
# for tc in range(1, T+1):
#     trash = input()
#     arr = list(map(int, input().split()))
#     num = 1
#
#     while arr[7] != 0:
#         if num == 6:
#             num = 1
#             arr[0] -= num
#             n = arr.pop(0)
#             arr.append(n)
#             num += 1
#         else:
#             arr[0] -= num
#             n = arr.pop(0)
#             arr.append(n)
#             num += 1
#         if arr[7] <= 0:
#             arr[7] = 0
#             break
#
#     arr = ' '.join(map(str, arr))
#
#     print(f'#{tc} {arr}')

# 강사님 풀이
T = 10
for tc in range(1, T+1):
    no = input()
    Q = list(map(int, input().split()))

    cnt = 0
    while True:
        temp = Q.pop(0)
        temp -= cnt % 5 + 1
        if temp < 0: temp = 0
        Q.append(temp)
        if temp == 0: break
        cnt += 1
    print(f'#{tc}', *Q)
