"""
Without using class
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for i in graph[start]:
        if i not in visited:
            dfs(graph, i, visited)
    return visited

graph = {0: [2], 1: [0,2], 2: [3], 3: [1,2]} 
dfs(graph, 1) # 1 0 2 3"""

class dfs:
    def __init__(self, graph):
        self.graph = graph
        self.visited = [False] * len(graph)
        self.stack = []

    def dfs(self, start):
        self.stack.append(start)
        self.visited[start] = True
        while self.stack:
            current = self.stack.pop()
            print(current, end=' ')
            for node in self.graph[current]:
                if not self.visited[node]:
                    self.stack.append(node)
                    self.visited[node] = True
graph = {0: [2], 1: [0,2], 2: [3], 3: [1,2]} 
mydfs=dfs(graph)
mydfs.dfs(0)
