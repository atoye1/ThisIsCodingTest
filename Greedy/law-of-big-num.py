n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()
print(numbers)
total = 0
current_k = k 
while m > 0:
    if current_k > 0:
        total += numbers[-1]
        current_k -= 1

    else:
        total += numbers[-2]
        current_k = k
    m -= 1
print(total)