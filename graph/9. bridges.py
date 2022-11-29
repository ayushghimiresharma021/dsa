from collections import defaultdict
class Graph:
    def __init__(self,vertices):
        self.v = vertices
        self.graph = defaultdict()
        self.time = 0
    def addEdges(self,u,v):
        self.graph[u].append(v)
        self.graph[u].append(v)
    def brides(self,par,parent,visited,low,disc):
        visited[par] = True
        low[par] =self.time
        disc[par] =self.time
        self.time+=1
        for child in self.graph[par]:
            if visited[child] == False:
                self.brides(child,parent,visited,low,disc)

                low[par] = min(low[child],low[par])

                if low[child]>disc[par]:
                    print(f'The bridge is {child} ')
            elif child!=parent[par]:
                low[par] = min(low[par],disc[child])


