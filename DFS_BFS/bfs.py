from collections import deque


def bfs(graph, start):
    visited = []
    q = deque([start])
    while q:
        current = q.popleft()
        if current not in visited:
            visited.append(current)
        q.extend([i for i in graph[current] if i not in visited])
    return visited


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

print(bfs(graph, 1))
