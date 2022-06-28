from collections import deque

N, M = map(int, input().split())
plate = []
for i in range(N):
    row = list(map(int, input()))
    plate.append(row)

count = 0


def dfs(x, y):
    if x < 0 or x > N - 1 or y < 0 or y > M - 1:
        return False
    if plate[x][y] == 0:
        plate[x][y] = 1
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True


def bfs(x, y):
    if x < 0 or x > N - 1 or y < 0 or y > M - 1:
        return False

    if plate[x][y] == 1:
        return False

    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        plate[x][y] = 1
        next_coords = [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]

        for coord in next_coords:
            x, y = coord[0], coord[1]
            if x < 0 or x > N - 1 or y < 0 or y > M - 1:
                continue
            if plate[x][y] == 0:
                q.append(coord)
    return True


for i in range(N):
    for j in range(M):
        if bfs(i, j):
            count += 1

print(count)
# plate의 첫번째 요소부터 탐색을 시작한다.
# 0을 만나면 인접한 모든 0을 특정한 값으로 바꾸고, 모든 인접한 0을 바꾼 후에는 count를 1증가시킨다.
# 리스트의 마지막 요소까지 반복한다.
