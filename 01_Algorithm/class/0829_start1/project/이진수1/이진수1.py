import sys
sys.stdin = open("이진수1_input.txt")

'''
A: 10
B: 11
C: 12
D: 13
E: 14
F: 15
'''

# T = int(input())
# for tc in range(1, T+1):
#     N, num = input().split()
#     dict = {
#         'A': 10,
#         'B': 11,
#         'C': 12,
#         'D': 13,
#         'E': 14,
#         'F': 15,
#     }
#     N = int(N)
#
#     # 문자 -> 숫자로 변환
#     num_arr = []
#     for string in num:
#         if string in dict:
#             num_arr.append(dict[string])
#         else:
#             num_arr.append(int(string))
#
#     # 16진수 -> 10진수로 표현하기
#     val = 0
#     for i in range(N):
#         val += num_arr[i] * (16**(N-i-1))
#
#
#     # 2진수로 만들기
#     result = []
#     while val != 0:
#         result.append(val % 2)
#         val //= 2
#
#     while len(result) < N:
#         result.append(0)
#
#     result = result[::-1]
#     result = ''.join(map(str, result))
#     print(f'#{tc} {result}')


# 강사님 풀이

hex_to_bin = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100',
    '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001',
    'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111',
}

T = int(input())
for tc in range(1, T + 1):
    n, arr = input().split()
    n = int(n)
    ans = ''
    for i in range(n):
        ans += hex_to_bin.get(arr[i])
    print(f'#{tc} {ans}')


