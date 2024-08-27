import sys
sys.stdin = open('문자열뒤집기_input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    text = str(input())
    result = ''
    for i in range(n-1, -1, -1):
        result += text[i]
    print(f'#{tc} {result}')


# 강사님 풀이
"""
str1 = 'algorithm'
arr = list(str1)
N = len(arr)
for i in range(N//2):
    arr[i], arr[N-1-i] = arr[N-1-i], arr[i]
str1 = ''.join(arr)
print(str1)
"""
