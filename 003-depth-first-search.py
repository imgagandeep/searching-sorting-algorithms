# Depth First Search algorithm

graph = {
    'A' : ['B', 'S'],
    'B' : ['A'],
    'C' : ['D', 'E', 'F', 'S'],
    'D' : ['C'],
    'E' : ['C', 'H'],
    'F' : ['C', 'G'],
    'G' : ['F', 'S'],
    'H' : ['E', 'G'],
    'S' : ['A', 'C', 'G'],
}

def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for i in graph[node]:
            dfs(graph, i, visited)
    return visited
visited = dfs(graph, 'A', [])
print(visited)
