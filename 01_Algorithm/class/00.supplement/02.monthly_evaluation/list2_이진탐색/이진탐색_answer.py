import sys
sys.stdin = open('이진탐색_input.txt')


def binary_search(arr, N, key):
    start, end = 1, N
    cnt = 0
    while start <= end:
        cnt += 1
        mid = (start + end) // 2
        if arr[mid] == key:
            return cnt
        elif arr[mid] > key:
            end = mid       # 기존의 이진탐색은 end = mid - 1
        else:
            start = mid     # 기존의 이진탐색은 start = mid + 1
    return -1               # 여기에 올 일은 없다. (검색 실패)


T = int(input())

for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    arr = [0] + list(range(1, P+1))
    a_cnt = binary_search(arr, P, A)
    b_cnt = binary_search(arr, P, B)

    ans = '0'
    if a_cnt > b_cnt:
        ans = 'B'
    elif a_cnt < b_cnt:
        ans = 'A'

    print(f'#{tc} {ans}')

