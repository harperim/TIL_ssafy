import sys
sys.stdin = open('flatten_input.txt', 'r')


def min_max(arr):
    min_i = max_i = 0
    for i in range(1, N):
        if arr[min_i] > arr[i]:
            min_i = i
        if arr[max_i] < arr[i]:
            max_i = i
    return max_i, min_i

T = 10

# max_idx, min_idx 구하기
# 평탄화 끝난 후, 최대최소값 구하기

for tc in range(1, T+1):

    N = 100
    dump = int(input())  # 834
    arr = list(map(int, input().split()))

    for i in range(dump):
        max_idx, min_idx = min_max(arr)
        arr[max_idx] -= 1
        arr[min_idx] += 1

    # 평탄화 후에 다시 최대, 최소 구하기
    max_idx, min_idx = min_max(arr)
    print(f'#{tc} {arr[max_idx]-arr[min_idx]}')






