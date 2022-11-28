from collections import defaultdict
class Graph:
    def __init__(self,vertices):
        self.v =vertices
        self.graph =[[] for i in range(vertices)]
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def bfs(self):
        visited = [False]*(self.v)
        arr =[]
        queue = []
        for i in range(self.v):
            if visited[i] == False:
                queue = []
                queue.append(i)
                visited[i] = True
                while queue:
                    s =queue.pop(0)
                    arr.append(s)
                    for j in self.graph[s]:
                        if visited[j]== False:
                            visited[j] = True
                            queue.append(j)