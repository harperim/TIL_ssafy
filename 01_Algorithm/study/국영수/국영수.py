import sys
sys.stdin = open('국영수_input.txt')

N = int(input())
arr = [list(input().split()) for _ in range(N)]

# 1, 2, 3번째 인덱스 정수형으로 변환
for a in arr:
    for i in range(4):
        if i != 0:
            a[i] = int(a[i])

def compare(a, b):
    # 국어 점수 (내림차순)
    if a[1] != b[1]:
        return b[1] - a[1]
    # 영어 점수 (오름차순)
    if a[2] != b[2]:
        return a[2] - b[2]
    # 수학 점수 (내림차순)
    if a[3] != b[3]:
        return b[3] - a[3]
    # 이름 (사전 순)
    return (a[0] > b[0]) - (a[0] < b[0])

# 버블 정렬을 이용한 직접 정렬 구현
n = len(arr)
for i in range(n):
    for j in range(i + 1, n):
        if compare(arr[i], arr[j]) > 0:
            # Swap if arr[i] should come after arr[j]
            arr[i], arr[j] = arr[j], arr[i]

for i in range(N):
    print(arr[i][0])


# # sorted를 사용해서 푼 경우
# arr_sorted = sorted(arr, key=lambda x: (-x[1], x[2], -x[3], x[0]))
#
# # 정렬된 리스트에서 0번째 인덱스 출력
# for i in range(N):
#     print(arr_sorted[i][0])





