import sys
sys.stdin = open('test_input.txt')


N, M = list(map(int, input().split()))  # N = 3, M = 3
arr = [list(map(int, input().split())) for _ in range(N)]

print(N, M)
# print(arr)

for i in range(len(arr)):  # len(arr) = 3, i = 0, 1, 2
    print(arr[i])


