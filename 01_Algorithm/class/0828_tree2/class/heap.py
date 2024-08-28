import heapq
# heap = [7, 2, 5, 3, 4, 6]
#
# # 최소힙
# # 한 번에 힙으로 변환
# heapq.heapify(heap)  # list -> heap
# print(heap)
# heapq.heappush(heap, 1)
# print(heap)
#
# while heap:
#     print(heapq.heappop(heap), end=' ')
# print()

# 최대힙 (음수로 표현)
temp = [7, 2, 5, 3, 4, 6]
heap2 = []
for i in range(len(temp)):
    heapq.heappush(heap2, -temp[i])
print(heap2)
heapq.heappush(heap2, -1)
print(heap2)
while heap2:
    print(heapq.heappop(heap2)*(-1), end=' ')


