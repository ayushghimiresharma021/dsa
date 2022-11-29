def shortest(vertices,adj,u,v):
    visited = [False]*vertices
    parent = [-1]*vertices
    queue = []
    queue.append(1)
    while queue:
        s = queue.pop()
        for i in adj[s]:
            if visited[i]==False:
                queue.append(i)
                visited[i] = False
                parent[i] = s
    end = v
    ans =[v]
    while end!=u or end!=-1:
         end = parent[end]
         ans.append(end)
    ans = ans[::-1]
         


        

        

