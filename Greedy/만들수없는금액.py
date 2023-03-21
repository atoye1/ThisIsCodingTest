from itertools import combinations
n = int(input())
nums = list(map(int, input().split()))
nums.sort()
answer = set()

# 조합을 활용한 완전탐색 해법
for i in range(1, n + 1):
    for combi in combinations(nums, i):
        answer.add(sum(combi))

for i in range(sum(nums)):
    if i not in answer:
        print(i)

# 탐욕법을 활용한 효율적인 해법
'''
1부터 차례대로 특정한 금액을 만들 수 있는지 확인하면 된다.
만약 1부터 target-1까지 만들 수 있다면
target 값을 업데이트하는 방식을 이용한다.
1, 2, 3, 8이라는 동전이 있다고 가정한다.
  1. 처음에는 1을 만들 수 있는지 확인한다.
  1-1. 화폐단위가 1인 동전이 있으므로 가능하다.
  2. 다음엔 2를 만들 수 있는지 가능하다.
  2-1. 우리에게는 화폐단위가 2인 동전이 있으므로
'''
target = 1
for x in nums:
    if target < x:
        break
    target += x
