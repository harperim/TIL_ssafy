import sys
sys.stdin = open('퍼펙트셔플_input.txt')


T = int(input())

# 홀수인 경우, 갈랐을 때 왼쪽을 한 장 더 주기
# 가져올 곳의 인덱스와 저장할 곳의 인덱스 따로 따로 저장
for tc in range(1, T+1):
    N = int(input())
    card = input().split()
    deck = [0] * N
    # print(arr)

    d = (N+1) // 2  # 아래에 오는 카드 시작 N//2+N%2

    i1 = 0
    i2 = d
    i3 = 0  # 새로 만들 덱
    while i3 < N:
        if i1 < d:
            deck[i3] = card[i1]
            i1 += 1
            i3 += 1
        if i2 < N:
            deck[i3] = card[i2]
            i2 += 1
            i3 += 1
    print(f'#{tc}', *deck)  # {*deck} 은 실행 안됨


