import sys
sys.stdin = open('돌뒤집기게임2_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    for _ in range(M):
        i, j = map(int, input().split())
        # two pointer
        left = right = i - 1  # idx - 1
        for _ in range(j):
            left -= 1
            right += 1
            # 범위 (index)
            if left < 0 or right >= N:
                break
            # 뒤집기
            if arr[left] == arr[right]:
                arr[left] = arr[right] = (arr[right]+1) % 2

    # result = ' '.join(map(str, arr))
    # print(f'#{tc} {result}')
    print(f'#{tc}', *arr)





