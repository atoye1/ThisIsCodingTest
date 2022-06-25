n, m = map(int, input().split())

bowls = list(map(int, input().split()))

count = 0
for i in range(n - 1):
    bowl_0 = bowls[i]
    for bowl_1 in bowls[i + 1:]:
        if bowl_0 != bowl_1:
            count += 1
print(count)
