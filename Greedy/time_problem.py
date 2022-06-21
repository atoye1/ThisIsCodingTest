import time


def countable(num) -> bool:
    if num == 0:
        return False
    if num % 10 == 3:
        return True
    if (num // 10) == 3:
        return True
    return False


n = int(input())
count = 0

start_time = time.time()
for hour in range(0, n+1):
    for minutes in range(0, 60):
        for sec in range(0, 60):
            if countable(hour):
                count += 1
                continue
            elif countable(minutes):
                count += 1
                continue
            elif countable(sec):
                count += 1
            else:
                pass

print(count)
end_time = time.time()
print(f"time elapsed: {start_time-end_time}")

count = 0
star_time = time.time()

for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)
end_time = time.time()
print(f"time elapsed: {start_time-end_time}")
