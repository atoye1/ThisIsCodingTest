import sys
from collections import deque

input = sys.stdin.readline
N, L, R = map(int, input().split())
nations = []
for i in range(N):
    nations.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(nations):
    day = 0
    while True:
        changed = False
        visited = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                # print("i, j : ", i, j)
                # 이미 탐색했던 곳이라면 건너뛴다.
                if visited[i][j] == 1:
                    continue
                # 방문하지 않았던 곳이면 이곳을 시작으로 bfs 수행하면서, 해당 지점의 값을 바꾼다.
                q = deque()
                q_elems = []
                q_sum = nations[i][j]
                q.append([i, j])
                q_elems.append([i, j])
                visited[i][j] = 1
                while q:
                    # print(q)
                    x, y = q.popleft()
                    for idx in range(4):
                        nx, ny = x + dx[idx], y + dy[idx]
                        if nx < 0 or ny < 0 or nx > N - 1 or ny > N - 1:
                            continue
                        if visited[nx][ny] == 1:
                            continue
                        if L <= abs(nations[x][y] - nations[nx][ny]) <= R:
                            changed = True
                            visited[nx][ny] = 1
                            q.append([nx, ny])
                            q_elems.append([nx, ny])
                            q_sum += nations[nx][ny]
                avg_pop = int(q_sum / len(q_elems))
                for x, y in q_elems:
                    nations[x][y] = avg_pop
        if not changed:
            return day
        day += 1


print(bfs(nations))
print(nations)
