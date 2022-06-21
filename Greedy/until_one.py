import time

n, k = map(int, input().split())
start_time = time.time()
count = 0

while (n != 1):
    if n % k == 0:
        n /= k
    else:
        n -= 1
    count += 1
end_time = time.time()
print("1", end_time - start_time)

start_time = time.time()

count = 0
while True:
    target = (n // k) * k
    count += (n - target)
    n = target
    if n < k:
        break
    count += 1
    n //= k

count += (n - 1)
print(count)

end_time = time.time()
print("2", end_time - start_time)
