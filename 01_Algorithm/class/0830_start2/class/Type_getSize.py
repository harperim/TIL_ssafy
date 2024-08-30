import sys
a = 1024

print(sys.getsizeof(a))  # 28byte
print(type(a))

a = 0xfffffff
print(sys.getsizeof(a))  # 28byte
print(type(a))

# 2진수로 먼저 바꾸기 / 149.625
# 10010101.101(2)
def get_binary(tar, n):
    bit = []
    while tar != 0:
        bit.append(tar % 2)
        tar //= 2

    while len(bit) < n:
        bit.append(0)
    return bit[::-1]

tar = 149.625
print(get_binary(tar, 8))
