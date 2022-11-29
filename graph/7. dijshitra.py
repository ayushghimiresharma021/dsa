MOD = 10000000000000
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        dist = [MOD]*V
        dist[S] = 0
        queue = [[0,S]]
        while queue:
            s = queue.pop()
            dis = s[0]
            u = s[1]
            for node,weight in adj[u]:
                if dis+weight<dist[node]:
                    dist[node] = dis+weight
                    queue.append([dist[node],node])
                    
        return dist
    
