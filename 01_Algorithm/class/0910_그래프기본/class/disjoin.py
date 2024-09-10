def make_set(x):
    p[x] = x

def find_set(x):
    if x == p[x]:
        return x
    else:
        return find_set(p[x])


def find_set2(x):
    while x != p[x]:
        x = p[x]
    return x

def union(x, y):  # x의 대표자, y의 대표자
    p[find_set(y)] = find_set(x)



N = 6
p = [0] * (N+1)  # 부모 저장
for i in range(1, N+1):
    make_set(i)


union(1, 3)
union(2, 3)
union(5, 6)
union(1, 6)
print(p)
print(find_set(6))

