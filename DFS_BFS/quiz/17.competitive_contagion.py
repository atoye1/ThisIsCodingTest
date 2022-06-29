import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
board = []
positions = [[] for _ in range(K + 1)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    for j, virus in enumerate(row):
        if virus != 0:
            positions[virus].append([i, j, 0])

S, X, Y = map(int, input().split())

# position에는 각 바이러스의 종류별로 위치한 좌표가 들어 있다.
# 1번 바이러스부터 차례대로 증식해 나가는데, 주변에 0이 있어야 증식이 된다.
# 만약 0이 없으면 다음 바이러스로 넘어간다.

time = 0
q = deque()

for position in positions:
    for elem in position:
        q.append(elem)
print(q)

while q:
    x, y, time = q.popleft()
    if time == S:
        break
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or ny < 0 or nx > N - 1 or ny > N - 1:
            continue
        if board[nx][ny] == 0:
            q.append([nx, ny, time + 1])
            board[nx][ny] = board[x][y]
print(board[X - 1][Y - 1])
