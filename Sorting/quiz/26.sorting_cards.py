import heapq

n = int(input())
heap = []
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)

result = 0

while len(heap) > 1:
    first = heapq.heappop()
    second = heapq.heappop()
    sub_total = first + second
    result += sub_total
    heapq.heappush(heap, sub_total)
print(result)
