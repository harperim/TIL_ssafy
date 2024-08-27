# (2)
import sys
sys.stdin = open('글자수_input.txt')

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    asc = [0] * 128
    alph = []
    max_val = 0

    # 중복제거
    for i in range(len(str1)):
        asc[ord(str1[i])] = 1   # ord 아스키코드로 바꾸는 함수 (65-a, 66-b, 67-c)

    for j in range(len(asc)):
        if asc[i]:
            alph.append(chr(i))

    # 카운팅
    asc = [0] * 128
    for i in range(len(str2)):
        for j in range(len(alph)):
            if str2[i] == alph[j]:
                asc[ord(str2[i])] += 1

    # 최대값
    for i in range(len(asc)):
        if max_val < asc[i]:
            max_val = asc[i]

    print(max_val)

