arr1 = [0] * 3

arr2 = [[0] * 3 for _ in range(2)]
print(arr1)  # [0, 0, 0]
print(*arr1)  # 0 0 0
print(arr2)  # [[0, 0, 0], [0, 0, 0]]

for i in range(2):
    print(arr2[i])
"""
[0, 0, 0]
[0, 0, 0]
"""
# -------------------------------
for i in range(2):
    for j in range(3):
        print(arr2[i][j], end = ' ')
    print()
"""
0 0 0
0 0 0
"""

arr = [[1, 2, 3], [4, 5, 6]]
print(len(arr))  # 2
print(len(arr[0]))  # 3

# arr을 아래처럼 만들면 X
# 0 0 0 을 arr[0], arr[1]이 가르킴
# => 같은 것을 가르키고 있기 때문에 하나의 값을 바꾸면 모두 바뀌어버림
arr = [[0] * 3] * 2
print(arr)  # [[0, 0, 0], [0, 0, 0]]
arr[0][0] = 1
print(arr)  # [[1, 0, 0], [1, 0, 0]]


