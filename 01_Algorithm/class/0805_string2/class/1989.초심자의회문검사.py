"""
- level과 같이 거꾸로 읽어도 제대로 읽은 것과 같은 문장이나 낱말을 회문(palindrome)이라 한다.
- 단어를 입력 받아 회문이면 1 출력, 아니라면 0 출력하는 프로그램 작성하기

3
level       #1 1
samsung     #2 0
eye         #3 1
"""

import sys
sys.stdin = open('1989_input.txt')

T = int(input())
for tc in range(1, T+1):
    s = input()
    N = len(s)
    ans = 1
    for i in range(N//2):
        if s[i] != s[N-1-i]:
            ans = 0
            break
    print(f'#{tc} {ans}')



