# def perm(n, k):
#     if n == k:
#         print(arr)
#     else:
#         for i in range(k, n):
#             arr[k], arr[i] = arr[i], arr[k]
#             perm(n, k+1)
#             arr[k], arr[i] = arr[i], arr[k]  # 되돌려놓기
#
#
# arr = [1, 2, 3]
# N = len(arr)
# perm(N, 0)

# 3 2 1 이 먼저 나옴


def perm(n, k, cursum):
    ##################################
    # 가지치기 위치 (재귀 돌기 전)
    ##################################
    if n == k:
        print(arr)
    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            perm(n, k+1, cursum + arr[k])
            arr[k], arr[i] = arr[i], arr[k]  # 되돌려놓기


arr = [1, 2, 3]
N = len(arr)
perm(N, 0, 4)   # cursum = ?
