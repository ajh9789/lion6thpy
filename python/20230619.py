#그래프 알고리즘
from collections import deque
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
visited = set()
#넓이우선
def bfs_iterative(start_node):
    queue = deque([start_node])
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            queue.extend(graph[node])
#깊이우선
def dfs_iterative(start_node):
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            stack.extend(reversed(graph[node]))

snode = 'A'
dfs_iterative(snode)
visited.clear()
print('\n-----')
bfs_iterative(snode)