# bfs를 활용해 최단경로를 구하는 문제이다.
from collections import deque

row, col = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(row)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(graph, start_row, start_col):
    q = deque()
    q.append((start_row, start_col))
    while q:
        curr_row, curr_col = q.popleft()
        for i in range(4):
            new_row = curr_row + dx[i]
            new_col = curr_col + dy[i]
            if new_row < 0 or new_row > row - 1 or new_col < 0 or new_col > col - 1:
                continue
            if graph[new_row][new_col] == 1:
                if new_row != 0 or new_col != 0:
                    graph[new_row][new_col] = graph[curr_row][curr_col] + 1
                    q.append((new_row, new_col))
    return graph[row - 1][col - 1]


print(bfs(graph, 0, 0))
print(graph)
