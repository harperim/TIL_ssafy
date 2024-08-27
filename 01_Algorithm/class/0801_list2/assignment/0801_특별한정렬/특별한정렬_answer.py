import sys
sys.stdin = open('특별한정렬_input.txt')


def solution_sort(arr, N):
    for i in range(N-1):
        if i % 2 == 0:
            idx = i
            for j in range(i+1, N):
                if arr[idx] < arr[j]:
                    idx = j
            arr[i], arr[idx] = arr[idx], arr[i]
        else:
            idx = i
            for j in range(i+1, N):
                if arr[idx] > arr[j]:
                    idx = j
            arr[i], arr[idx] = arr[idx], arr[i]


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]




