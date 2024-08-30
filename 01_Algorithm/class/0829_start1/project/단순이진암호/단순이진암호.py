import sys
sys.stdin = open('단순이진암호_input.txt')

mapping_code = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3,
                '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7,
                '0110111': 8, '0001011': 9,
                }


def find_pos(arr):
    for i in range(N):
        for j in range(M - 1, -1, -1):
            if arr[i][j] == 1:
                return i, j


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]

    sx, sy = find_pos(arr)
    sy -= 55

    # dict에서 암호 코드 찾기
    pwd = []
    for i in range(8):
        pwd.append(mapping_code.get(''.join(map(str, arr[sx][sy:sy + 7]))))
        sy += 7

    # 검증하기
    odd = pwd[0] + pwd[2] + pwd[4] + pwd[6]
    even = pwd[1] + pwd[3] + pwd[5] + pwd[7]
    if (odd * 3 + even) % 10 == 0:
        print(f'#{tc} {odd + even}')
    else:
        print(f'#{tc} {0}')



