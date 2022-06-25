n = int(input())
coins = list(map(int, input().split()))
coins.sort()

if coins[0] != 1:
    print(1)
else:
    sum = 1
    for i in range(1, n):
        new_sum = sum + coins[i]
