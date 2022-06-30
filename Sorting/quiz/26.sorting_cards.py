import heapq
import sys

input = sys.stdin.readline
n = int(input())
heap = []

for i in range(n):
    heapq.heappush(heap, int(input()))
result = 0
while len(heap) != 1:
    first = heapq.heappop(heap)
    second = heapq.heappop(heap)
    sub_total = first + second
    result += sub_total
    heapq.heappush(heap, sub_total)

print(result)
