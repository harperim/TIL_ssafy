import sys
sys.stdin = open('문자열비교_input.txt')

"""
수도코드
for i in range(n-m+1):
    flag = 1
    for j in range(m):
        if p[i+j] != p[j]:  # 같지 않으면 중지
        flag = 0
            break
    if :
        return i
    flag가 1이면 return
return -1
"""

# T = int(input())
#
# for tc in range(1, T+1):
#     short = str(input())
#     long = str(input())
#
#     n = len(short)
#     m = len(long)
#
#     for i in range(m-n+1):
#         flag = 1
#         correct = 0
#         for j in range(n):
#             if long[i+j] != short[j]:
#                 flag = 0
#                 break
#             else:
#                 correct += 1
#         if correct == n:
#             break
#     print(f'#{tc} {flag}')

# 강사님 풀이
T = int(input())

def my_find(pat, txt):
    n = len(txt)
    m = len(pat)
    for i in range(n-m+1):
        flag = 1
        for j in range(m):
            if txt[i+j] != pat[j]:
                flag = 0
                break
        if flag: return 1
    return 0               # 원래 find 값


for tc in range(1, T+1):
    pat = str(input())
    txt = str(input())

    print(f'#{tc} {my_find(pat, txt)}')
