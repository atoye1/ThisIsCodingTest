import sys
from itertools import permutations


def calculate(nums, case):
    sub_total = nums[0]
    for i in range(len(case)):
        if case[i] == 0:
            sub_total += nums[i + 1]
        elif case[i] == 1:
            sub_total -= nums[i + 1]
        elif case[i] == 2:
            sub_total *= nums[i + 1]
        elif case[i] == 3:
            if sub_total < 0:
                sub_total *= -1
                sub_total //= nums[i + 1]
                sub_total *= -1
            else:
                sub_total //= nums[i + 1]
        else:
            assert False
    return sub_total


input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))  # +, -, *, //
temp = []
for num, count in enumerate(operators):
    while count > 0:
        temp.append(num)
        count -= 1
operators = temp
cases = permutations(operators)

max_result = 0
min_result = float('inf')
for case in cases:
    case_result = calculate(nums, case)
    max_result = max(max_result, case_result)
    min_result = min(min_result, case_result)

print(max_result)
print(min_result)
