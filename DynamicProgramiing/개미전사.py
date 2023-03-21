n = int(input())
storages = list(map(int, input().split()))
memo = [0 for _ in range(n)]
# memo = [0] * n

for idx, elem in enumerate(storages):
    if idx == 0 or idx == 1:
        memo[idx] = storages[0]
    # 현 시점의 최대 구간합은 현재 elem와 두개 전 요소의 구간합을 더한것과, 한개 전 요소의 구간합중 큰걸 선택한다.)
    memo[idx] = max(elem + memo[idx - 2], memo[idx - 1])
print(memo[-1])
