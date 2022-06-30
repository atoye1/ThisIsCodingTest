n = int(input())
houses = list(map(int, input().split()))

houses.sort()
mid = (n - 1) // 2
print(houses[mid])
