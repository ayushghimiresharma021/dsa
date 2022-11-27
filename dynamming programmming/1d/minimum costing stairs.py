##1.Total no of possiblites to climb a stairs 

def minimumdp(n,dp):
    if n<=1:
        return 1
    if dp[n]!=-1:
        return dp[n]
    dp[n] = minimumdp(n-1,dp)+minimumdp(n-2,dp)
    return dp[n]
n = int(input('number ? '))
dp = [-1]*(n+1)
print(minimumdp(n,dp))

2.

def minimumcost(cost,dp,n):
    if n == 0:
        return cost[0]
    if n == 1:
        return cost[1]
    if dp !=-1:
        return dp[n]
    dp[n] = min(minimumcost(cost,dp,n-1),minimumcost(cost,dp,n-2))
    return dp[n]


def mincosttabulation(cost):
    n = len(cost)
    dp = [-1]*(n+1)
    dp[0] = [cost[0]]
    dp[1] = [cost[1]]
    for i in range(2,n):
        dp[i] = min(dp[i-1],dp[i-2])+cost[i]
    return min[dp[n-1],dp[n-2]]
