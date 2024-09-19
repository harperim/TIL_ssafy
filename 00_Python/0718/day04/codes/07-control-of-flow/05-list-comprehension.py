# 사용 전
numbers = [1, 2, 3, 4, 5]
squared_numbers = []

for num in numbers:
    squared_numbers.append(num**2)

print(squared_numbers)


# 사용 후
squared_numbers2 = []
squared_numbers2 = [num ** 2 for num in numbers]
print(squared_numbers2)

# List Comprehension 활용 예시 - "2차원 배열 생성 시 (인접행렬 생성 시)"
arr = [0] * 5
print(arr)
data1 = [[0] * 5 for _ in range(5)]
data1[0][0] = 100
print(data1)
# 또는
data2 = [[0 for _ in range(5)] for _ in range(5)]
data2[0][0] = 100
print(data2)

data3 = [[0] * 5] * 5  # 이렇게 하면 안 됩니다.
data3[0][0] = 100
print(data3) 

# 사용전
result = []
for i in range(10):
    if i % 2 == 1:
        result.append(i)
print(result)
# 사용후
result2 = [i for i in range(10) if i % 2 == 1]
print(result2)