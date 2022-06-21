N, M, K = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort(reverse=True)
result = 0
idx = 0
new_M = M

"""
    M인 전체 반복횟수가 소진될 때까지 정렬된 리스트의 첫 번째와 두 번째 리스트를 번갈아가면서 더한다.
"""

while M > 0:
    if M > K:
        if idx == 0:
            result += nums[idx] * K
            M -= K
            idx = 1
        else:
            result += nums[idx]
            M -= 1
            idx = 0
    else:
        if idx == 0:
            result += nums[idx] * M
        else:
            result += nums[idx]
            M -= 1
            idx = 0

print(result)


"""
    수열의 패턴을 파악해서 아래와 같이 작성하면 성능향상 가능하다.
"""

M = new_M
first = nums[0]
second = nums[1]
first_count = (M // (K+1)) * K + M % (K + 1)
second_count = M - first_count
result = first*first_count + second*second_count
print(result)
