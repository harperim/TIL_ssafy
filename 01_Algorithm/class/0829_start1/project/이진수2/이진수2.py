import sys
sys.stdin = open('이진수2_input.txt')


def get_bin(num):
    result = ''
    cnt = 0

    while num != 0 and cnt < 13:
        num *= 2
        cnt += 1
        if num >= 1:
            result += '1'
            num -= 1
        else:
            result += '0'

    # 어떤 조건에서 탈출했는지 구분해야 함
    if cnt >= 13:
        return 'overflow'
    else:
        return result


T = int(input())
for tc in range(1, T + 1):
    num = float(input())
    print(f'#{tc} {get_bin(num)}')
