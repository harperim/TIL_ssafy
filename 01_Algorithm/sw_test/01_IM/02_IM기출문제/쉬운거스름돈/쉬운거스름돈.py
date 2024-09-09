import sys
sys.stdin = open('쉬운거스름돈_input.txt')

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     type = [0] * 8
#
#     while N > 0:
#         if N >= 50000:
#             type[0] = N // 50000
#             N = N - (N // 50000)*50000
#         elif N >= 10000:
#             type[1] = N // 10000
#             N = N - (N // 10000)*10000
#         elif N >= 5000:
#             type[2] = N // 5000
#             N = N - (N // 5000)*5000
#         elif N >= 1000:
#             type[3] = N // 1000
#             N = N - (N // 1000)*1000
#         elif N >= 500:
#             type[4] = N // 500
#             N = N - (N // 500)*500
#         elif N >= 100:
#             type[5] = N // 100
#             N = N - (N // 100)*100
#         elif N >= 50:
#             type[6] = N // 50
#             N = N - (N // 50)*50
#         elif N >= 10:
#             type[7] = N // 10
#             N = N - (N // 10)*10
#     print(f'#{tc}')
#     print(*type)

# 다른 친구 풀이
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    change = [50000,10000,5000,1000,500,100,50,10]
    result = []
    for i in change:
        result.append(N // i)
        N = N % i  # 나머지를 계산해 남은 금액을 업데이트
    print(f'#{tc}')
    print(*result)
