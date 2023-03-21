n, m = map(int, input().split())

coins = []

for _ in range(n):
    coins.append(int(input()))

'''
coins에 있는 화폐를 최소한으로 활용해서 m원을 만드는 것이 목표다.
점화식을 세워봐야하나?
만약 m이 coins 안에 있는 동전과 동일하면, 한번에 가능하다.
'''
# 최소한 만들 수 있는 금액은 min(coins)

memo = [10001] * (m + 1)  # 메모를 초기화 한다.

if m < min(coins):
    print(-1)
else:
    # m원을 만들 때 까지 메모에다 기록하면서 탐색한다.
    for i in range(min(coins), m + 1):  # 이중 루프를 돈다. O(n * m) 시간을 사용한다. 백만이하라서 가능
        if i in coins:  # 만약 갖고있는 코인종류와 동일한 금액이면, 1개만 가지고도 가능하다.
            memo[i] = 1
            continue
        # 현재 숫자에서 코인종류를 하나씩 뺀 값에 해당하는 메모가 활성화되어 있으면 그 메모 + 1 해주면 된다
        for coin in coins:
         # 한번에 min으로 비교해주기 위해서 초깃값을 10001로 이론상 가장 큰 값으로 잡았다.
         # 만약 0이나 -1로 초깃값을 지정해준 경우 해당 값인 경우는 min()을 사용하지 않도록 해야 한다.
            if memo[i - coin] != 10001:
                memo[i] = min(memo[i], memo[i - coin] + 1)
print(memo)
print('answer : ', memo[m])
