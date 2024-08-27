# 정렬되어 있지 않은 경우
def sequential_search(a, n, key):  # a : 리스트, n = 리스트 길이, key = 찾아야 하는 숫자

    # for문 실행 제대로 안되니까 수정해보기
    # for i in range(n):
    #     if a[i] == key:
    #         return i
    #     else:
    #         return -1

    i = 0
    while i < n and a[i] != key:  # 인덱스 검사 먼저하고, 접근하기
        i += 1
    if i < n:
        return i
    else:
        return -1


print(sequential_search([4, 9, 11, 23, 2, 19, 7], 7, 2))  # 성공 / idx = 4


# 정렬된 경우
def sequentialSearch2(a, n, key):
    i = 0
    while i < n and a[i] < key:
        i += 1
    if i < n and a[i] == key:
        return i
    else:
        return -1


print(sequentialSearch2([2, 4, 7, 9, 11, 19, 23], 7, 10))  # 실패 / -1


# 이진 검색
def binarySearch(a, N, key):
    start = 0
    end = N-1

    while start <= end:
        middle = (start+end)//2
        if a[middle] == key:   # 검색 성공
            return True
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return False                 # 검색 실패


print(binarySearch([2, 4, 7, 9, 11, 19, 23], 7, 20))  # 실패 / False


# 선택 정렬 과정
def SelectionSort(arr, n):  # arr 정렬 대상 / N 크기
    # 주어진 구간에 대해 기준 위치 i 정하기
    for i in range(n-1):
        min_idx = i         # 최소값 위치를 기준위치로 가정
        for j in range(i+1, n):         # 남은 원소에 대해 실제 최소값 위치 검색
            if arr[min_idx] > arr[j]:
                min_idx = j
        # 구간의 최소값을 기준 위치로 이동
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


A = [2, 7, 5, 3, 4]
B = [4, 3, 2, 1]
SelectionSort(A, len(A))
SelectionSort(B, len(B))
print(A)
print(B)

# 라이브방송 수업 코드
# ---------------------------------------
# 실습 코드


# 순차검색
def seq_search(arr, N, key):
    for i in range(N):
        if arr[i] == key:
            return i   # idx return
    return -1  # -1이 접근이 되기 때문에 조심하기!


arr = [4, 9, 11, 23, 2, 29, 7]
N = len(arr)
key = 8
print(seq_search(arr, N, key))

if seq_search(arr, N, key) != -1:
    print('찾았다')  # 1
else:
    print('못찾았다')  # 0

# for 문 2개 빠져나가려면 return으로 빠져나가기!
# nxn 행렬에서 원하는 값 찾으면 빠져나가는 문제인 경우 : return으로 빠져나가기


# 이진 검색 - 사전 찾기와 비슷! 중간 탁 잘라서 찾아보는 것
def binary_search(arr, N, key):
    start = 0
    end = N - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == key:  # 1. key == mid일 때(찾았을 때)
            return mid  # key가 mid를 기준으로 왼편에 있을 때
        elif arr[mid] > key:  # 2. key가 mid를 기준으로 오른편에 있을 때
            end = mid - 1
        else:  # 3. key가 mid 오른편에 있을 때
            start = mid + 1
    return -1  # 다 돌았는데 못 찾은 경우 (검색 실패)


arr = [2, 4, 7, 9, 11, 19, 23]
N = len(arr)
key = 7
print(binary_search(arr, N, key))  # 2


# 선택정렬 -> 파괴적 메서드 : 원본이 바뀌기 때문
def selection_sort(a, N):
    for i in range(N-1):
        # 최소값 (idx)
        min_idx = i
        for j in range(i+1, N):
            if a[min_idx] > a[j]:
                min_idx = j
        # i값 <-> 최소값(idx)
        a[i], a[min_idx] = a[min_idx], a[i]

def selection(a, N, k):  # k번 돌면 됨
    for i in range(N-1):
        # 최소값 (idx)
        min_idx = i
        for j in range(i+1, N):
            if a[min_idx] > a[j]:
                min_idx = j
        # i값 <-> 최소값(idx)
        a[i], a[min_idx] = a[min_idx], a[i]
    return arr[k-1]


arr = [64, 25, 10, 22, 11]
N = len(arr)
selection_sort(arr, N)
print(arr)  # [10, 11, 22, 25, 64] ; 파괴적 메서드라 값이 변경됨
print(selection(arr, N, 2))
print(arr)



