"""
without using class
def bfs(graph, root):
    visited, queue = set(), [root]
    visited.add(root)
    while queue: 
        vertex = queue.pop(0)
        print(vertex)
        for neighbour in graph[vertex]: 
            if neighbour not in visited: 
                visited.add(neighbour) 
                queue.append(neighbour) 

graph = {0: [2], 1: [0,2], 2: [3], 3: [1,2]} 
bfs(graph, 2) # return 2 3 1 0
"""

class bfs:
    def __init__(self, graph):
        self.graph = graph
        self.visited = [False] * len(graph)
        self.queue = []

    def bfs(self, root):
        self.queue.append(root)
        self.visited[root] = True
        while self.queue:
            current = self.queue.pop(0)
            print(current, end=' ')
            for node in self.graph[current]:
                if not self.visited[node]:
                    self.queue.append(node)
                    self.visited[node] = True

graph = {0: [2], 1: [0,2], 2: [3], 3: [1,2]}
mybfs=bfs(graph)
mybfs.bfs(0) # return 0 2 3 1