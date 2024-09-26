import sys
sys.stdin = open('01knapsack_input.txt', 'r')


T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    V = []
    C = []
    dp = [[0 for i in range(K+1)] for j in range(N+1)]
    for i in range(N):
        v, c = map(int, input().split())
        V.append(v)
        C.append(c)  # 입력받기

    for i in range(1, N+1):  # 물건 선택
        for k in range(1, K+1):  # 가방의 크기 K까지의
            if k >= V[i-1]:  # 가방에 물건이 들어간다면
                dp[i][k] = max(dp[i-1][k-V[i-1]]+C[i-1], dp[i-1][k])
            else:  # 가방에 물건이 들어가지 않는다면
                dp[i][k] = dp[i-1][k]
    print(f'#{test_case} {dp[N][K]}')  # 1부터 N까지의 물건중 K만큼의 크기를 만족시키는 가장 큰 값

