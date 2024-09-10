import sys
sys.stdin = open('쇠막대기자르기_input.txt')

T = int(input())
for tc in range(1, T + 1):
    stick = input()
    stick_sum = 0
    stack = []

    for i in range(len(stick)):
        if stick[i] == '(':
            stack.append('(')
        else:
            stack.pop()
            if stick[i - 1] == '(':
                stick_sum += len(stack)
            else:
                stick_sum += 1

    print(f'#{tc} {stick_sum}')
