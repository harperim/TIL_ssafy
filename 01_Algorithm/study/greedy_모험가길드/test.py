import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
lst = list(map(int, input().split()))

lst.sort(reverse=True)  # 3 2 2 2 1

size = lst[0]  # 3
count = 0

for i in range(len(lst)):  # 0 1 2 3 4
    if (i+1) % size == 0:
        count += 1  # 3
        if len(lst)-(i+1) > 0:
            size = lst[i+1]

print(count)
        
