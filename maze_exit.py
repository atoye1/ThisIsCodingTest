# p.152
from collections import deque

n, m = map(int, input().split())
maze = []
for _ in range(n):
    row = [int(c) for c in input()]
    maze.append(row)

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def bfs(maze, coords):
    q = deque()
    q.append(coords)
    while q:
        x, y = q.popleft()
        curr_val = maze[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx > n - 1 or ny > m - 1:
                continue
            print(nx, ny)
            if maze[nx][ny] == 1:
                maze[nx][ny] += curr_val
                q.append((nx, ny))


bfs(maze, (0, 0))
print(maze[n-1][m-1])
