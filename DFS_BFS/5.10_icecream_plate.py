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


for i in range(N):
    for j in range(M):
        if dfs(i, j):
            count += 1

print(count)
# plate의 첫번째 요소부터 탐색을 시작한다.
# 0을 만나면 인접한 모든 0을 특정한 값으로 바꾸고, 모든 인접한 0을 바꾼 후에는 count를 1증가시킨다.
# 리스트의 마지막 요소까지 반복한다.
