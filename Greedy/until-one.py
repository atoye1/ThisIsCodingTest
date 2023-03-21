n, k = map(int, input().split())
count = 0

while n >= k:
    q, r = divmod(n, k)
    count += 1 + r
    n = q
count += n - 1

print(count)
