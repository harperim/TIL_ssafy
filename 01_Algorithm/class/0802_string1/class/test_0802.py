s1 = list(input())  # 1234
s2 = input()        # 1234

print(s1)  # ['1', '2', '3', '4']
print(s2)  # 1234

s = input()  # 1234
print(s[0])  # 1
print(s[1])  # 2  바로 인덱스 접근 가능


s1 = 'abc'
s2 = 'abc'
print(s1 == s2)  # True

l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 == l2)  # True

s3 = s1[:2] + 'c'
print(s3)  # abc
print(s2 == s3)  # True
print(s2 is s3)  # False
print(s1 is s2)  # True

# -----------------------
s1 = 'A'
print(ord('A'))  # 65
print(ord(s1))   # 65

print(chr(65))  # A

s = '123'


def atoi(s):
    i = 0
    for x in s:
        i = i*10 + ord(x) - ord('O')
    return i



# 연습문제2 ; str()함수 사용하지 않고, itoa() 구현해보기