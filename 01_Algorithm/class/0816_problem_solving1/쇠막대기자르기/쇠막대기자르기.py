import sys
sys.stdin = open('쇠막대기자르기_input.txt')

T = int(input())

for tc in range(1, T+1):
    stick = list(input())
    stack = []
    cnt = 0

    for s in stick:
        if s == '(':
            stack.append(s)
        else:
            if len(stack) > 0:
                stack.pop()
                cnt += 1
    print(cnt)




