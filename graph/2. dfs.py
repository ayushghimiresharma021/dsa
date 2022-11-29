from collections import defaultdict
class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.graph = defaultdict()
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def dfs(self,vertex,visited,arr):
        visited[vertex] = True
        arr.append(vertex)
        for i in range(self.graph[vertex]):
            if visited[i] == False:
                self.dfs(i,visited,arr)
    def dfsuntil(self):
        visited = [False]*(self.vertices)
        arr =[]
        for i in range(self.vertices):
            if visited[i] == False:
                self.dfs(i,visited,arr)
                