# 재귀함수로 구현
# 방문은 print로 표현

def dfs_recursive(graph, start, visited, result=[]):
    # 스타트 노드 방문처리한다
    if len(result) >= len(visited):
        return result
    visited[start] = True
    # 방문 처리된 노드는 한번 출력해준다.
    result.append(start)
    # 현재 방문한 노드와 인접한 노드가 있으면 해당 노드를 대상으로
    for i in graph[start]:
        if not visited[i]:
            return dfs_recursive(graph, i, visited, result=result)
    # 재귀적으로 dfs를 실시한다.


def dfs_stack(graph, start):
    stack = [start]
    visited = []
    while stack:
        curr = stack.pop()
        if curr not in visited:
            visited.append(curr)
        for i in graph[curr][::-1]:
            if i not in visited:
                stack.append(i)
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

print(dfs_stack(graph, 1))
print(dfs_recursive(graph, 1, visited=[False for _ in range(9)], result=[]))
