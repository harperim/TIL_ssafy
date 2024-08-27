import sys
sys.stdin = open('공과잡초_input.txt')

# (1)
T = int(input())

for tc in range(1, T+1):
    ball = input()
    count = 0
    for k in ball:      # ball 문자열을 순회하면서
        if k == '(' or k == ')':    # 문자열에 '('나')'가 있으면
            count += 1      # 카운트 횟수 추가
    print(f'#{tc} {count - ball.count("()")}')  # 만약에 ()가 붙어 있으면


# (2)
T = int(input())
for tc in range(1, T+1):
    s = input()
    cnt = 0
    i = 0
    while i < len(s):
        if s[i]==')':   #  () |) (|
            cnt += 1
        elif s[i-1]=='(' and s[i]=='|': # (|
            cnt += 1
        i += 1
    print(f'#{tc} {cnt}')


