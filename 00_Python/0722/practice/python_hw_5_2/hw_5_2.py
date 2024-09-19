# 아래 함수를 수정하시오.
def count_character(text, key):
    return text.count(key)


def count_character2(text, key):
    cnt = 0
    for ch in text:
        if ch == key:
            cnt += 1
    return cnt


result = count_character("Hello, World!", "o")
print(result)  # 2

result = count_character2("Hello, World!", "o")
print(result)  # 2
