n, M = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(n)]
# 무게 이익 순으로 입력된다.

items.sort(key=lambda x: x[1]/x[0], reverse=True)
# 단위 무게당 이익순으로 리스트를 정렬함 O(nlogn)의 시간복잡도

value_sum = 0

for item in items:
    print(value_sum)
    if M >= item[0]:
        value_sum += item[1]
        M -= item[0]
    else:
        value_sum += item[1] / item[0] * M
        M = 0
        break
print(value_sum)
