from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

goal = input("Enter goal node: ").upper()

queue = deque([['A']])
visited = set()

while queue:
    path = queue.popleft()
    node = path[-1]

    if node in visited:
        continue

    visited.add(node)

    if node == goal:
        print("BFS Traversal:", " ".join(visited))
        print("Goal found")
        print("Path:", " -> ".join(path))
        break

    for child in graph[node]:
        if child not in visited:
            queue.append(path + [child])
else:
    print("Goal not found")
