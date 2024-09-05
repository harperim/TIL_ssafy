import sys
sys.stdin = open('퀵정렬_input.txt')

def partition(a, l, r):
    pivot = a[l]
    i, j = l, r
    while i < j:  # i, j 가 cross 되면 stop
        # i가 피벗보다 큰 값 찾기
        while a[i] <= pivot and i < r:
            i += 1
        # j가 피벗보다 작은 값 찾기
        while a[j] >= pivot and j > l:
            j -= 1
        if i < j:
            a[i], a[j] = a[j], a[i]  # 작은 값 큰 값 찾았으므로 자리 바꾸기
    # 피벗을 가운데로 옮기기
    a[l], a[j] = a[j], a[l]
    return j  # 피벗의 위치


def quick_sort(a, l, r):
    if l < r:  # 하나 남을 때까지
        pivot = partition(a, l, r)
        quick_sort(a, l, pivot-1)
        quick_sort(a, pivot+1, r)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    quick_sort(A, 0, N - 1)  # 인덱스의 범위를 넣어야 함
    print(f'#{tc} {A[N//2]}')
