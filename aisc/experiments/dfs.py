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
visited = set()
path = []

def dfs(node):
    visited.add(node)
    path.append(node)

    if node == goal:
        return True

    for child in graph[node]:
        if child not in visited:
            if dfs(child):
                return True

    path.pop()
    return False

if dfs('A'):
    print("DFS Traversal:", " ".join(visited))
    print("Goal found")
    print("Path:", " -> ".join(path))
else:
    print("Goal not found")
