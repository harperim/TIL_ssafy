import sys
sys.stdin = open('이진탐색_input.txt')


def binary_search(a, n, key):
    left, right = 0, n - 1
    dir = -1  # 0:왼쪽, 1:오른쪽
    while left <= right:
        mid = (left + right) // 2
        if key == a[mid]:
            return 1
        elif key < a[mid]:  # 왼쪽방향
            if dir == 0:
                return 0
            else:
                right = mid - 1
                dir = 0
        else:
            if dir == 1:
                return 0
            else:
                left = mid + 1
                dir = 1

    return 0


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    cnt = 0
    for i in range(M):
        cnt += binary_search(A, N, B[i])
    print(f'#{tc} {cnt}')
