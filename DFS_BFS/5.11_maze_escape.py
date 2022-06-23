from collections import deque

N, M = map(int, input().split())
maze = []
for i in range(N):
    maze.append(list(map(int, input())))

# monster = 0, no monster = 1
# bfs활용해서 풀이해 나간다. bfs 진행하면서 1씩 증가시키면 된다.

# 동서남북형태의 무빙 벡터 정의
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    q.append((x, y))
    while q:
        curr_x, curr_y = q.popleft()

        for i in range(4):
            nx = curr_x + dx[i]
            ny = curr_y + dy[i]

            if nx < 0 or nx > N - 1 or ny < 0 or ny > M - 1:
                continue
            if maze[nx][ny] == 0:
                continue
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[curr_x][curr_y] + 1
                q.append((nx, ny))


q = deque()
bfs(0, 0)

print(maze[N - 1][M - 1])
