from itertools import combinations

n, m = map(int, input().split())
city = []
for i in range(n):
    city.append(list(map(int, input().split())))
houses = []
chickens = []


def calc_distance(house, chicken):
    return abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])


for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            houses.append((i, j))
        elif city[i][j] == 2:
            chickens.append((i, j))
city_distances = []

candidate = list(combinations(chickens, m))

for case in candidate:
    city_distance = 0
    for house in houses:
        distance = float('inf')
        for chic in case:
            curr_distance = calc_distance(house, chic)
            if curr_distance < distance:
                distance = curr_distance
        city_distance += distance
    city_distances.append(city_distance)

print(min(city_distances))

# 치킨집 M개 각각에 대해서 각 집과의 거리를 구하여 정렬한다?
# 각 집과의 거리가 가장 먼 치킨집부터 제거해 나간다.
# 각 집과의 거리를 이미 계산 해 놓은 테이블에서 뽑아오는 형식으로 중복된 계산을 줄인다?
