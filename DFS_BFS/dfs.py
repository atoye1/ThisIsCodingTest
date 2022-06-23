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

# dfs는 스택을 이용한다.
# 첫 번째 원소를 스택에 넣고, 그 원소와 인접한 가장 가까운 원소를 스택에 넣어가며 재귀적으로 탐색해 나간다.
# 스택에 있는 노드의 모든 인접노드들이 방문했던 노드라면 해당 노드를 스택에서 pop하고 그 다음 노드를 대상으로 DFS 한다.
# 스택이 빌 때 까지 계속한다.
# 재귀함수는 스택프레임을 활용하므로 굳이 스택을 구현하지 않아도 dfs 구현 가능하다.

visited = [False for _ in range(9)]


def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')
    for node in graph[start]:
        if not visited[node]:
            dfs(graph, node, visited)


dfs(graph, 1, visited)
