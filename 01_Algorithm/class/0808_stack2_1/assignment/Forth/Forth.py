import sys
sys.stdin = open("Forth_input.txt")

# str1 = [10, 2, +, 3, 4, +, *, .]
def forth(str1):
    stack = []
    for tok in str1:        # 문자열을 순회
        # 피연산자 : push
        if tok.isdigit():
            stack.append(tok)
        # 연산자 : pop x 2
        elif tok == '+' or tok == '-' or \
            tok == '*' or tok == '/':
            # tok in '-+*/'
            if len(stack) < 2:      # 스택 안에 2개 이상 존재
                return 'error'
            else:
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                if tok == '+':
                    stack.append(op1 + op2)
                elif tok == '-':
                    stack.append(op1 - op2)
                elif tok == '*':
                    stack.append(op1 * op2)
                elif tok == '/':
                    stack.append(op1 // op2)
        # 점 (.) : 계산 결과를 리턴
            # 스택 안에 1개만 존재
        elif tok == '.':
            if len(stack) == 1:
                return stack.pop()
            else:
                return 'error'

# 후위 표기법을 스택을 이용해서 계산
T = int(input())

# 먼저 꺼낸걸 뒤에 놓기
# 2개 꺼내야 하는데 2개가 되지 않는 경우 error
# . 하나만 존재
for tc in range(1, T+1):
    str1 = list(input().split())
    print(f'#{tc} {forth(str1)}')

