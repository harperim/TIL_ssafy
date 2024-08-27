import sys
sys.stdin = open('괄호검사01_input.txt')


def matching(s):
    stack = []  # append, pop 사용할 빈 리스트
    for item in s:
        # 소괄호인 경우
        # 1. 왼쪽괄호 -> push
        if item == '(' or item == '{':
            stack.append(item)
        # 2. 오른쪽 ->
        elif item == ')' or item == '}':
            # 2-1. isEmpty -> return 0
            if len(stack) == 0:     # if not stack = stack이 비어있으면
                return 0
            # 2-2. else -> pop()
            else:
                tmp = stack.pop()

                if item == ')' and tmp != '(':
                    return 0
                elif item == '}' and tmp != '{':
                    return 0
    # 3. 검사 후 Not IsEmpty -> return 0
    if stack:
        return 0
    else:
        return 1


T = int(input())

for tc in range(1, T+1):
    string = list(str(input()))
    print(f'#{tc} {matching(string)}')

