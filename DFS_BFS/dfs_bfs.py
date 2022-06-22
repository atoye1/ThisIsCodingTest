
from collections import deque

graph = [  # 쉬운 인덱싱을 위해 첫 번째 을 비워둠
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

# 방문 내역을 기록하기 위한 리스트를 구현한다.


def dfs(graph, node, visited):
    visited[node] = True
    print(node)
    for i in graph[node]:
        if not visited[i]:
            visited[i] = True
            dfs(graph, i, visited)

# 처음 노드를 선택한다.
# 해당 노드와 연결된 모든 노드가 방문되지 않은 노드인 경우 차례로 큐에 넣는다.
# 큐에서 pop()연산한 노드를 대상으로 BFS를 계속 수행한다.


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


visited = [False for _ in range(len(graph))]
dfs(graph, 1, visited)

visited = [False for _ in range(len(graph))]
q = deque()
bfs(graph, 1, visited)
