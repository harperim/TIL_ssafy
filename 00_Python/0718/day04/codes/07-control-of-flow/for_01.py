# 2중 for문을 이용하여 구구단을 작성하시오.(for, range)
'''
### 2단 ###
2 * 1 = 2
2 * 2 = 2
...
### 3단 ###
3 * 1 = 3
'''
for i in range(2, 10):
    print(f'### {i}단 ###')
    for j in range(1, 10):
        print(f'{i} * {j} = {i*j}')