import sys
sys.stdin = open('회문1_input.txt')

T = 10
N = 8

def r_count(arr):
    cnt = 0
    for i in range(N):
        for j in range(N-M+1):
            flag = 1
            for k in range(M//2):
                if arr[i][j+k] != arr[i][j+M-1-k]:
                    flag = 0
                    break
            if flag:
                cnt += 1
    return cnt

def c_count(arr):
    cnt = 0
    for i in range(N):
        for j in range(N-M+1):
            flag = 1
            for k in range(M//2):
                if arr[j+k][i] != arr[j+M-1-k][i]:
                    flag = 0
                    break
            if flag:
                cnt += 1
    return cnt


# flag 안 쓰려면 else 사용
for tc in range(1, T+1):
    M = int(input())
    arr = [list(map(str, input())) for _ in range(N)]
    # arr = [list(input()) for _ in range(N)]

    cnt = 0
    cnt += r_count(arr)
    cnt += c_count(arr)
    print(f'#{tc} {cnt}')

