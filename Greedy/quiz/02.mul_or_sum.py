s = input()
result = 0
for num in s:
    num = int(num)
    if num == 0 or num == 1 or result == 0:
        result += num
    else:
        result *= num
print(result)
