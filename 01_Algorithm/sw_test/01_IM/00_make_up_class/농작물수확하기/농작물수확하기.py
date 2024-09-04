import sys
sys.stdin = open('농작물수확하기_input.txt')

T = int(input())

# 행마다 돌면서 열은 좌우로 하나씩 추가하거나 감소
dj = [-1, 1]

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    idx = []
    idx.append(N // 2)
    sum_val = 0
    for i in range(N):
        for j in range(N):
            # 하나씩 증가하기
            if i < 2//N:
                length = i % (N//2)
                for k in range(1, length+1):
                    pass
            # 다 더하기
            elif i == 2//N:
                pass
            # 하나씩 감소하기
            else:
                pass




