from collections import Counter
ball_count, max_weight = map(int, input().split())
balls = list(map(int, input().split()))
# 완전탐색으로 무식하게 구하기
answer = set()
for i in range(0, ball_count - 1):
    for j in range(i, ball_count):
        if balls[i] != balls[j] and (j, i) not in answer:
            answer.add((i, j))
print(len(answer))

# 카운터를 활용해서 그리디로 구하기
# 무게 1부터 무게 1이 들어가는 모든 경우의 수를 구한다.
# 무게 2부터는 무게 1인 원소들이 제외된 경우를 대상으로 무게 2를 선택한 모든 경우의 수를 구한다.
# 무게 3부터 반복하고 누적합을 구한다.
result = 0
c = Counter(balls)
for i in range(1, max_weight + 1):
    ball_count -= c[i]
    result += c[i] * ball_count
print(result)
