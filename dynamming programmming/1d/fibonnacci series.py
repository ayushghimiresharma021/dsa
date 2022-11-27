def fibo(n,dp):
    if n<=1:
        return n
    if dp[n] !=-1:
        return dp[n]
    dp[n] = fibo[n-1]+fibo[n-2]
    return dp[n]
def fibo1(n):
    dp = [-1]*n+1
    dp[0] = 0
    dp[1] = 0
    for i in range(2,len(dp)):
        dp[i] = dp[i-1]+dp[i-2]
    

