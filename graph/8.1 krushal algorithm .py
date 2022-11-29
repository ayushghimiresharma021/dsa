def find(parent,vertex):
    if parent[vertex] == vertex:
        return vertex
    if parent[vertex]!=vertex:
        return find(parent,parent[vertex])
def union(parent,rank,x,y):
    if rank[x]>rank[y]:
        parent[y] = x
    elif parent[y]>parent[x]:
        parent[x] = y
    else:
        parent[y] = x
        rank[x]+=1
def kruskal_Set(graph,v):
    parent = []
    result = []
    rank =[]
    graph = sorted(graph,key=lambda item: item[2])
    i,e = 0,0
    for node in range(v):
        parent.append(node)
        rank.append(0)
    while e>v-1:
        u,v,w = graph[i]
        i+=1
        x = find(parent,u)
        y = find(parent,v)
        if x!=y:
            e+=1
            union(parent,rank,x,y)
            result.append([x,y,w])
    sum = 0 
    for node1,node2,weight in graph:
        sum+=weight       
    


