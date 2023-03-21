def fib_rcsv(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    else:
        return fib_rcsv(num - 1) + fib_rcsv(num - 2)


def fib_dp(num):
    result = [0, 1]
    for i in range(2, num + 1):
        result.append(result[i - 2] + result[i - 1])
    return result[num]


for i in range(50):
    print(fib_dp(i))
print('dp done')
for i in range(50):
    print(fib_rcsv(i))
