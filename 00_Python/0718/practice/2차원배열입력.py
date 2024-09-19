#  2차원배열 초기화
arr =  [[0] * 3  for _ in range(3)]
print(arr)

'''
2 3
1 2 3
4 5 6
'''
# 2차원배열 입력
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(arr)

'''
2 3
010
100
'''
# 2차원배열 입력
N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
print(arr)