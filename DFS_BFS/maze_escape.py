from collections import deque
N, M = map(int, input().split())
maze = []
for i in range(N):
    maze.append(list(map(int, input())))
# monster = 0, no monster = 1

row, col = 0, 0
q = deque()

maze[x][y]

if x - 1 >= 0 or x - 1 <= N - 1:
    if maze[x - 1][y] != 0:
        maze[x - 1][y] = maze[x][y] + 1
    return False
if x + 1 >= 0 or x + 1 <= N - 1:
    if maze[x + 1][y] != 0:
        maze[x + 1][y] = maze[x][y] + 1
    return False
if x - 1 >= 0 or x - 1 <= N - 1:
    if maze[x - 1][y] != 0:
        maze[x - 1][y] = maze[x][y] + 1
    return False
if x - 1 >= 0 or x - 1 <= N - 1:
    if maze[x - 1][y] != 0:
        maze[x - 1][y] = maze[x][y] + 1
    return False
maze[x - 1][y]
maze[x + 1][y]
maze[x][y + 1]
maze[x][y - 1]
