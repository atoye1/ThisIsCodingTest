import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
maze = []
for i in range(N):
    maze.append(list(map(int, input().strip())))

# bfs활용해서 풀이해 나간다. bfs 진행하면서 1씩 증가시키면 된다.

# 동서남북형태의 무빙 벡터 정의
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(maze):
    q = deque()
    q.append((0, 0))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx > - 1 or ny > M - 1:  # 범위를 벗어난 곳으로 이동 못함
                continue
            if maze[nx][ny] == 0:  # 괴물이 있으면 못감
                continue
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                q.append((nx, ny))


bfs(maze)
print(maze)
print(maze[N-1][M-1])
