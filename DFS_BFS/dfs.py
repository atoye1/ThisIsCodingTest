# 탐색 시작 노드를 스택에 삽입하고 방문처리
# 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리한다. 인접한 노드가 없으면 해당 노드를 꺼낸다
# 2번의 과정이 수행되지 않을때 까지 반복한다.

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[v]:
            dfs(graph, i, visited)


def dfs(graph, start):
    visited = set()         # create a set to store visited vertices
    stack = [start]         # create a stack to store unexplored vertices
    while stack:
        vertex = stack.pop()    # get the next unexplored vertex from the top of the stack
        if vertex not in visited:
            visited.add(vertex)    # mark the vertex as visited
            # do whatever you want with the vertex here, such as print it
            # print(vertex)
            # add unvisited neighboring vertices to the stack
            stack.extend(graph[vertex] - visited)
    return visited
