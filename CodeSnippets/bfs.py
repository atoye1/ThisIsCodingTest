from collections import deque
# 너비 우선 탐색


def bfs(graph, start, visited):
    q.append(start)
    visited[start] = True
    while q:
        cur_node = q.popleft()
        print(cur_node, end=' ')
        for i in graph[cur_node]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


if __name__ == "__main__":

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
    # 큐를 활용한다.
    # 첫번째 노드와 인접한 모든 노드 중 미방문한 모든 큐에 삽입한다.
    # 큐에 삽입된 노드는 표시하여 재 삽입되지 않도록 한다.
    # 다음 노드 탐색시 해당 노드와 인접한 미표시된 노드를 큐에 삽입한다.

    q = deque()
    visited = [False] * 9
    print(visited)
    bfs(graph, 1, visited)  # 1 2 3 8 7 4 5 6
