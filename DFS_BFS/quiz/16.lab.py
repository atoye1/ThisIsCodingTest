import sys
from collections import deque
from itertools import combinations


input = sys.stdin.readline

N, M = map(int, input().split())
lab_map = []
empty_space = []

for i in range(N):
    row = list(map(int, input().split()))
    lab_map.append(row)
    for j in range(M):
        if row[j] == 0:
            empty_space.append([i, j])
# input handling done

# define custom variables
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(lab_map):
    q = deque()
    for i in range(N):
        for j in range(M):
            if lab_map[i][j] == 2:
                q.append([i, j])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx > N - 1 or ny > M - 1:
                continue
            if lab_map[nx][ny] == 0:
                lab_map[nx][ny] = 2
                q.append([nx, ny])


def count_safe_zone(lab_map):
    count = 0
    for i in range(N):
        for j in range(M):
            if lab_map[i][j] == 0:
                count += 1
    return count


cases = combinations(empty_space, 3)
max_safe_zones = 0
for case in cases:
    case_lab_map = [b[:] for b in lab_map]
    for x, y in case:
        assert case_lab_map[x][y] == 0
        case_lab_map[x][y] = 1
    bfs(case_lab_map)
    now_safe_zones = count_safe_zone(case_lab_map)
    if max_safe_zones < now_safe_zones:
        max_safe_zones = now_safe_zones
print(max_safe_zones)
