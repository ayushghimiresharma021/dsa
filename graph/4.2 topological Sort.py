
def topologicalUsingDfs(v, stack, visited, graph):
    # for the topological we only use one slight change to ds that is we add an array at the end of the code so that w when the code is ended it adds all the 
    visited[v] = True
    for i in graph[v]:
        if visited[i] ==False:
            topologicalUsingDfs(i,stack,visited,graph)
    stack.append(v)
def topological_Using_Dfs_Until(v,graph):
    visited = [False]*v
    stack =[]
    for i in range(v):
        if visited[i]==False:
            topologicalUsingDfs(i,stack,visited,graph)
    return stack

def topological_sort_bfs_kahm(vertices,graph):
    visited = [False]*vertices
    in_order = [0]*vertices
    for i in range(vertices):
        for j in graph[i]:
            in_order[i]+=1
    queue = []
    for i in range(len(in_order)):
        if in_order[i]==0:
            queue.append(i)
        top_order = []
    while queue:
        u = queue.pop()
        top_order.append(u)
        for v in graph[u]:
            in_order[i]-=1
            if in_order[i]==0:
                queue.append(i)
        




