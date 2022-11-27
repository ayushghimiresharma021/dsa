def knapsack(weight,value,index,capacity,dp):
    if index==0:
        if weight[0]<=capacity:
            return value[0]
        else:
            return 0
    if dp[index][capacity]!=-1:
        return dp[index][capacity]
    include =0 
    if weight[index-1]<=capacity:
        include = value[index-1]+knapsack(weight,value,index-1,capacity-weight[index-1],dp)
    exclude = knapsack(weight,value,index-1,capacity,dp)
    dp[index][capacity] = max(include,exclude)
    return dp[index][capacity]
def tableknapsack(w,weight,value,n):
    dp = [[0 for i in range(w+1)] for j in range(n+1)]
    for i in range(n+1):
        for wt in range(w+1):
            if i == 0 or wt ==0:
                dp[i][wt] = 0
            elif weight[i-1]<=wt:
                include = value[i-1]+dp[i-1][wt-wt[i-1]]
                exclude = dp[i-1][w]
                dp[i][wt] = max(include,exclude)
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][w]
# here we can see that the current row  is depend on only on i-1 so we can only just make an 2 arrays with one being i-1 and another being i
def tablewithlessSpace(w,weight,value,n):
    prev = [0 for i in range(w+1)]
    curr = [0 for j in range(w+1)]
    for i in range(n+1):
        for wt in range(w+1):
            if i == 0 or wt ==0:
                prev[w] = 0
            elif weight[i-1]<=wt:
                include = value[i-1]+prev[wt-wt[i-1]]
                exclude = prev[w]
                curr[i] = max(include,exclude)
            else:
                curr[i] = prev[w]
        prev = curr
N = 3
W = 4
values = [1,2,3]
weight = [4,5,1]
dp = [ [-1 for i in range(W+1)] for j in range(N+1) ]
print(knapsack(value=values,weight=weight,index=N,capacity=W,dp=dp))

        




        



        