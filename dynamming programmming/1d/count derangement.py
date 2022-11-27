def derangement(arr,n,dp):
    if n==1:
        return 0
    if n == 2:
        return 0
    if dp[n]!=-1:
        return dp[n]
    dp[n] =(n-1)*(derangement(arr,n-1)+derangement(arr,n-2))
    return dp[n]
def usingTable(arr):
    n = len(arr)
    dp = [0]*(n+1)
    dp[1]=0
    dp[2]=1
    for i in range(3,n+1):
        prev1 = dp[i-1]
        prev2 = dp[i-2]
        sum  = prev1+prev2
        ans =(n-1)*sum


