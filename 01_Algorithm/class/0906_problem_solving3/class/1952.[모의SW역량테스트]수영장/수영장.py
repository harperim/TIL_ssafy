import sys
sys.stdin = open('수영장_input.txt')

# 시작점 : 1월 / 누적금액 : 0원
# 끝점 : 12월
def dfs(month, sum_cost):
    global ans
    # 기저조건. 12월까지 모두 보았는가?
    if month > 12:
        ans = min(ans, sum_cost)
        return

    # 1일권으로 모두 구매(다음 재귀 : 다음 달을 확인)
    dfs(month + 1, sum_cost + (days[month] * cost[0]))

    # 1달권 구매 (다음 재귀 : 다음 달을 확인)

    # 3달권 구매 (다음 재귀 : 3달 후을 확인)

    # 1년권 구매(다음 재귀 : 12달 후를 확인)

for tc in range(1, T+1):
    cost = list(map(int, input().split()))
    days = [0] + list(map(int, input().split()))

