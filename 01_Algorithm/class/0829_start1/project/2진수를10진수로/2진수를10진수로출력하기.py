import sys
sys.stdin = open('2진수를10진수로출력하기_input.txt')


def solve(arr):
    cnt = 0
    for i in range(7):
        if arr[i] == 1:
            cnt += 2 ** i
    return cnt


T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input()))
    arr = arr[::-1]
    lst = []

    for i in range(0, len(arr), 7):
        lst.append(solve(arr[i:i + 7]))

    print(f'#{tc}', *lst[::-1])


