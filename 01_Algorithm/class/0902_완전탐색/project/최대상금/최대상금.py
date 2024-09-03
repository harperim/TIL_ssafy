import sys
sys.stdin = open('최대상금_input.txt')

# 완전탐색으로 풀기

def dfs(lev, arr):
    global ans
    # 0. 가지치기
    money = int(''.join(arr))
    if (money, lev) in visited:
        return
    else:
        visited.append((money, lev))
    # 1. 기저조건
    if lev == N:
        ans = max(ans, int(''.join(arr)))
        return  # return 없으면 else 써야 함 = return 쓰면 else 안 써도 됨
    # 유도파트
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            arr[i], arr[j] = arr[j], arr[i]
            dfs(lev + 1, arr)
            arr[i], arr[j] = arr[j], arr[i]

T = int(input())
for tc in range(1, T+1):
    arr, N = map(str, input().split())
    arr = list(arr)  # str -> list
    visited = []
    N = int(N)
    ans = 0
    dfs(0, arr)
    print(f'#{tc} {ans}')
