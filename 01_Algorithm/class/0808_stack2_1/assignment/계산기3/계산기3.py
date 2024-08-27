import sys
sys.stdin = open('계산기3_input.txt')

# 강사님 코드 (미완성)
# # 스택 밖의 왼쪽 괄호는 우선순위가 가장 높으며, 스택 안의 왼쪽 괄호는
#
# def infix_to_postfix(infix):
#     stack = []
#     result = ''     # 후위 표기식을 저장
#     # 1. 입력 받은 중위 표기식에서 토큰을 읽는다.
#     for tok in infix:
#         # 2. 토큰이 피연산자이면 토큰을 출력한다.
#         if '0' <= tok <= '9':
#             result += tok
#         # 3. 토큰이 연산자(괄호포함)일 때,
#         elif tok == '(' or tok == '+' or tok == '-' or tok == '*' or tok == '/':
#             # 이 토큰이 스택의 top에 저장되어 있는 연산자보다 우선순위가 높으면 스택에 push하고,
#             # 그렇지 않다면 스택 top의 연산자의 우선순위가 토큰의 우선순위보다 작을 때까지 스택에서 pop한 후 토큰의 연산자를 push
#             # 만약 top에 연산자가 없으면 push한다.
#             if stack:
#                 while icp[tok] <= isp[stack[-1]]:
#                     result += stack.pop()
#                     if not stack: break
#                 stack.append(tok)
#             else:
#                 stack.append(tok)
#
#         # 4. 토큰이 오른쪽 괄호 ')'이면 스택 top에 왼족 괄호 '('가 올 때까지 스택에 pop연산을 수행하고 pop한 연산자를 출력한다.
#         # 왼쪽 괄호를 만나면 pop만 하고 출력하지는 않는다.
#         elif tok == ')':
#             while stack[-1] != '(':
#                 result += stack.pop()
#             stack.pop()     # 왼쪽 괄호 버리기
#
#     # 스택에 남아있는

T = 10
for tc in range(1, T + 1):
    N = int(input())
    string = input()
    stack = []
    result = ''
    for i in string:
        if i.isdigit():  # 피연산자인지 아닌지 확인
            result += i
        else:
            if i == '(':
                stack.append(i)
            elif i == '*':
                while stack and stack[-1] == '*':
                    result += stack.pop()
                stack.append(i)
            elif i == '+':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.append(i)
            elif i == ')':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.pop()
    while stack:
        result += stack.pop()

    stack = []
    for i in result:
        if i == '+':
            stack.append(stack.pop() + stack.pop())
        elif i == '*':
            stack.append(stack.pop() * stack.pop())
        else:
            stack.append(int(i))

    print('#{} {}'.format(tc, stack.pop()))
