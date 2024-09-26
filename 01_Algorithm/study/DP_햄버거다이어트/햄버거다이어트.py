import sys
sys.stdin = open('햄버거다이어트_input.txt', 'r')


def select_burger(burgers, cal_limit):
    n = len(burgers)  # 5
    dp = [[0 for _ in range(cal_limit + 1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, cal_limit + 1):
            score, cal = burgers[i-1]  # 현재 햄버거의 점수와 칼로리 / 100 200
            if cal <= j:  # 현재 햄버거의 칼로리가 칼로리 제한 j 이하일 경우
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-cal] + score)  # 선택할 때와 선택하지 않을 때의 최대 점수를 비교
            else:
                dp[i][j] = dp[i-1][j]  # 선택할 수 없으므로 이전 햄버거의 값을 그대로 사용
    return dp[n][cal_limit]  # 최대 점수 반환환

T = int(input())
for test_case in range(1, T + 1):
    burger_num, cal_limit = map(int, input().split())
    burger_lst = []
    for i in range(burger_num):
        score, cal = map(int, input().split())
        burger_lst.append((score, cal))
    res = select_burger(burger_lst, cal_limit)  # 최대 점수 계산
    print(f"#{test_case} {res}")


'''
cal_limit와 n의 값
- cal_limit + 1 = 1000 + 1 = 1001
- n + 1 = 5 + 1 = 6

dp = [
    [0, 0, 0, ..., 0],  # dp[0][0]부터 dp[0][1000]까지 (모두 0)
    [0, 0, 0, ..., 0],  # dp[1][0]부터 dp[1][1000]까지 (모두 0)
    [0, 0, 0, ..., 0],  # dp[2][0]부터 dp[2][1000]까지 (모두 0)
    [0, 0, 0, ..., 0],  # dp[3][0]부터 dp[3][1000]까지 (모두 0)
    [0, 0, 0, ..., 0],  # dp[4][0]부터 dp[4][1000]까지 (모두 0)
    [0, 0, 0, ..., 0]   # dp[5][0]부터 dp[5][1000]까지 (모두 0)
]
'''