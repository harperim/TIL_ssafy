import sys
sys.stdin = open('러시아국기같은깃발_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(N)]



# 다른 사람 풀이
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    result = 9999999999
    white = 0
    for w in range(N - 2):
        for k in range(M):
            if arr[w][k] != 'W':
                white += 1

        blue = 0
        for b in range(w + 1, N - 1):
            for k in range(M):
                if arr[b][k] != 'B':
                    blue += 1

            red = 0
            for r in range(b + 1, N):
                for k in range(M):
                    if arr[r][k] != 'R':
                        red += 1

            result = min(result, white + blue + red)

    print(f'#{tc} {result}')

