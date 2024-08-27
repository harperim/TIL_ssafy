import sys
sys.stdin = open('반복문자지우기_input.txt')

def delete_same(string):
    box = []

    for s in string:
        if len(box) == 0:
            box.append(s)
        else:
            if box[-1] == s:
                box.pop()
            else:
                box.append(s)
    return len(box)


T = int(input())

for tc in range(1, T+1):
    string = input()
    print(f'#{tc} {delete_same(string)}')
