from collections import deque
def cycle_Detection_bfs_undirected_graph(vertices,graph):
    parent =[-1]*vertices
    visited = [False]*vertices

    for i in range(vertices):
        queue = deque()
        queue.append(i)
        visited[i] = True
        while queue:
            u = queue.pop()
            for v in graph[u]:
                if visited[v]==False:
                    parent[u] = v
                    visited[u] = True
                elif parent[u]!=v:
                    return True
    return False

def cycledetectionUsingDfs(v,graph,visited,parent):
    visited[v] = True
    for i in graph[v]:
        if visited[i]==False:
            if cycle_Detection_bfs_undirected_graph(i,graph,visited,parent):
                return True
        elif parent!=i:
            return True
    return False