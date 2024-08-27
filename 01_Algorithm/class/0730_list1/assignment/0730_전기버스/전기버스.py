import sys
sys.stdin = open('전기버스_input.txt', 'r')

T = int(input())

# 충전할 수 없는 경우
def solve(charge, k, n, m):  # 3 10 5
    # 시작 정류장과 도착 정류장 추가
    charge = [0] + charge + [n]
    last = cnt = 0  # 마지막 충전기 번호
    for i in range(1, m+2):
        # 충전 하지 못해서 도착 정류장에 올 수 없는 경우
        # 두 충전기 사이가 k보다 크면 충전할 수 없음
        if charge[i] - charge[i-1] > k:
            return 0
        if charge[i] > last + k:
            last = charge[i-1]
            cnt += 1
    return cnt


for tc in range(1, T+1):
    # K:한 번 충전으로 이동 가능한 정류장 수
    # N:정류장 수 = 도착 정류장
    # M:충전기가 설치된 정류장 수
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))
    ans = solve(charge, K, N, M)
    print(f'#{tc} {ans}')


