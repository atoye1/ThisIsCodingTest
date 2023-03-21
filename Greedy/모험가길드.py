import sys
n = int(input())
group = list(map(int, input().split()))
answer = 0
# 내림차순으로 정렬해서 pop()하면서 서브그룹을 만든다.
group.sort(reverse=True)

group_count = 0

while group:
    max_score = group.pop()
    group_count += 1
    if max_score <= group_count:
        answer += 1
        group_count = 0
print(answer)
