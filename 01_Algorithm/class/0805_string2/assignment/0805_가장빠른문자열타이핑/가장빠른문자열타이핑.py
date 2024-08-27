import sys
sys.stdin = open('가장빠른문자열타이핑_input.txt')

T = int(input())

# for tc in range(1, T+1):
#     word, s_word = map(str, input().split())
#     n = len(word)
#     m = len(s_word)
#     count = 0
#
#     idx = 0
#     if idx < n-m+1:  # n-m+1 = 3
#         for _ in range(n-m+1):
#             if word[idx:idx+m] == s_word:
#                 count += 1
#                 idx = idx+m
#             else:
#                 count += 1
#                 idx += 1
#         print(f'#{tc} {count}')


# 강사님 풀이
def my_find(txt, pat, n, m):
    cnt = 0
    i = 0      # 초기화

    while i < n-m+1:     # 조건식
        flag = 1
        for j in range(m):
            if txt[i+j] != pat[j]:
                flag = 0
                break
        if flag:
            cnt += 1
            i = i + m - 1   # 찾은 패턴 이후로 인덱스 변경 (+m : 패턴의 길이만큼 점프)
        i += 1              # 증감식
    return cnt


for tc in range(1, T+1):
    txt, pat = map(str, input().split())
    n, m = len(txt), len(pat)
    cnt = my_find(txt, pat, n, m)
    ans = n - m * cnt + cnt
    print(f'#{tc} {ans}')

# -------------------------
# i+=2 무시하고 0~9까지 출력
# for i in range(10):
#     print(i)
#     i += 2
#
#
# for i in range(10):
#     print(i)



