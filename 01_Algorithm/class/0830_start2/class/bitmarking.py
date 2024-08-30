visited1 = [1, 0, 0, 0, 1]
visited2 = 0b10001
print(visited2, bin(visited2))

# 원소 추가
visited = 0
visited = visited | 1 << 3


# 원소 제거
visited = visited & ~(1 << 3)
print(visited)

# 원소 조회
visited = visited | 1 << 3
print(visited & (1 << 3))
visited = visited & ~(1 << 3)
print(visited & (1 << 3))

# 원소 토글
visited = visited ^ (1 << 3)
print(visited)
