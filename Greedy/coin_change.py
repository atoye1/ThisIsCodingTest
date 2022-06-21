import sys

# money = int((sys.stdin.readline()))
money = 1260
coins = [10, 50, 100, 500]

coins.reverse()
for coin in coins:
    count = money // coin
    print(f"{coin} {count}개")
    money %= coin
