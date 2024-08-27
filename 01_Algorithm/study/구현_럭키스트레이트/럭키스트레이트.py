import sys
sys.stdin = open('럭키스트레이트_input.txt')

num = list(map(int, input()))  # 1 2 3 4 0 2

left_sum = 0
right_sum = 0

for i in range(len(num)):  # 0 1 2 3 4 5
    if i < len(num)//2:
        left_sum += num[i]
    else:
        right_sum += num[i]

if left_sum == right_sum:
    answer = 'LUCKY'
else:
    answer = 'READY'

print(answer)
