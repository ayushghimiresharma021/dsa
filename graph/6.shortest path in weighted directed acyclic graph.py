MOD = -1000000001-1
def topological_sort(visited,stack,vertex,adj):
    visited[vertex] = True
    for node,weight in adj[vertex]:
        if visited[node]==False:
            topological_sort(visited,stack,i,adj)
        stack.append(vertex)
def shortesPath(adj,s,vertices):
    visited = [False]*vertices
    stack = []
    topological_sort(visited,stack,0,adj)
    dist = [MOD]*vertices
    dist[s] = 0
    while stack :
        i = stack.pop(0)
        for node,weight in adj[i]:
            if dist[node]>dist[node]+weight:
                dist[node] = dist[node]+weight


    
    
    
    