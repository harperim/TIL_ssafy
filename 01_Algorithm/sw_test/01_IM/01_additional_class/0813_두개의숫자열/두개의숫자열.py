import sys
sys.stdin = open('두개의숫자열_input.txt')

# float('-Inf') : 메모리 많이 차지하니까 되도록이면 지양

T = int(input())

for tc in range(1, T+1):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    sum_v = 0

    if len(a) > len(b):
        n = a       # 길이가 더 긴 리스트
        m = b       # 길이가 더 짧은 리스트
    else:
        n = b       # 길이가 더 긴 리스트
        m = a       # 길이가 더 짧은 리스트

    len_n = len(n)
    len_m = len(m)

    for i in range(len(n)-len(m)+1):
        for j in range(len(m)):
            sum_v += n[i] * m[j]
            print(sum_v)




