import sys
sys.stdin = open('쇠막대기자르기_input.txt')

T = int(input())
for tc in range(1, T + 1):
    stick = input()
    stick_sum = 0
    stack = []

    for i in range(len(stick)):  # ()(((()())(())()))(())
        if stick[i] == '(':
            stack.append('(')
        else:
            stack.pop()
            # 전체를 절단하는 부분이므로 전체 막대기의 개수만크므 더하기
            if stick[i - 1] == '(':
                stick_sum += len(stack)
            # 여기서 막대기의 길이가 끝난다는 의미이므로 +1
            else:
                stick_sum += 1

    print(f'#{tc} {stick_sum}')
