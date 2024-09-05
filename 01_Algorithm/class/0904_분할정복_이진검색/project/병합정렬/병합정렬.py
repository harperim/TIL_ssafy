import sys
sys.stdin = open('병합정렬_input.txt')

from collections import deque


def merge(left, right):
    left = deque(left)
    right = deque(right)
    result = []
    # 병합과정 : 각각의 최소값들(가장 왼쪽값)을 비교해서 더 작은 요소를 결과에 추가
    while left or right:
        # 두 부분집합의 요소가 모두 남아 있는 경우
        if left and right:
            if left[0] <= right[0]:
                result.append(left.popleft())
            else:
                result.append(right.popleft())

        elif left:  # 왼쪽만 있는 경우
            result.append(left.popleft())
        elif right:  # 오른쪽만 있는 경우
            result.append(right.popleft())

    return result


def merge_sort(a):
    global cnt
    # 1. 기저조건
    if len(a) == 1:
        return a
    # 2. 유도파트
    else:  # 절반으로 나눈어서 각각 별도의 정렬 실행
        mid = len(a) // 2
        left = a[:mid]  # 30
        right = a[mid:]  # 2

        left = merge_sort(left)  # 10 69   # 2 10 30 69
        right = merge_sort(right)  # 2 30

        if left[-1] > right[-1]:
            cnt += 1

        return merge(left, right)  # 2 10 30 69


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))

    cnt = 0
    A = merge_sort(A)
    print(f'#{tc} {A[N // 2]} {cnt}')