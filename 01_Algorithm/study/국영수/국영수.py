import sys
sys.stdin = open('국영수_input.txt')

# (1) 시간 초과
# N = int(input())
# arr = [list(input().split()) for _ in range(N)]
#
# # 1, 2, 3번째 인덱스 정수형으로 변환
# for a in arr:
#     for i in range(4):
#         if i != 0:
#             a[i] = int(a[i])
#
# def compare(a, b):
#     # 국어 점수 (내림차순)
#     if a[1] != b[1]:
#         return b[1] - a[1]
#     # 영어 점수 (오름차순)
#     if a[2] != b[2]:
#         return a[2] - b[2]
#     # 수학 점수 (내림차순)
#     if a[3] != b[3]:
#         return b[3] - a[3]
#     # 이름 (사전 순)
#     return (a[0] > b[0]) - (a[0] < b[0])
#
# n = len(arr)
# for i in range(n):
#     for j in range(i + 1, n):
#         if compare(arr[i], arr[j]) > 0:
#             # Swap if arr[i] should come after arr[j]
#             arr[i], arr[j] = arr[j], arr[i]
#
# for i in range(N):
#     print(arr[i][0])

# (2)
N = int(input())
arr = [list(input().split()) for _ in range(N)]

# 1, 2, 3번째 인덱스 정수형으로 변환
for a in arr:
    for i in range(4):
        if i != 0:
            a[i] = int(a[i])

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        idx = i
        for j in range(i + 1, n):
            # 국어 내림차순, 영어 오름차순, 수학 내림차순, 이름 오름차순
            if (arr[j][1] > arr[idx][1]) or \
               (arr[j][1] == arr[idx][1] and arr[j][2] < arr[idx][2]) or \
               (arr[j][1] == arr[idx][1] and arr[j][2] == arr[idx][2] and arr[j][3] > arr[idx][3]) or \
               (arr[j][1] == arr[idx][1] and arr[j][2] == arr[idx][2] and arr[j][3] == arr[idx][3] and arr[j][0] < arr[idx][0]):
                idx = j
        # 가장 큰 값 현재 위치와 교환
        arr[i], arr[idx] = arr[idx], arr[i]

# 데이터 정렬
selection_sort(arr)

# 정렬된 데이터에서 이름만 출력
for item in arr:
    print(item[0])


