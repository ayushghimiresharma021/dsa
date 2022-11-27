def maximumSum(arr,n,dp):
    if n<0:
        return 0
    if n == 0:
        return arr[0]
    if dp[n] !=-1:
        return dp[n]

    incl = maximumSum(arr,n-2,dp)+arr[n]
    excl = maximumSum(arr,n-1,dp)+0
    dp[n]=max(incl,excl)
    return dp[n]
def usingtabale(arr):
    n = len(arr)
    dp = [0]*(n)
    dp[0] = arr[0] 
    for i in range(1,n):
        inclu = dp[i-2]+arr[i]
        exclu = dp[i-1]
        dp[i] = max(inclu,exclu)
    return dp[n-1]
def withspace(num):
    n= len(num)
    dp = [0]*(n)
    prev1 = 0
    prev2 = num[0]
    for i in range(1,n):
        inclu = prev1+sum
        exclu = prev2
        ans = max(inclu,exclu)
        pre1 = prev2
        prev2 = ans 
    return prev2




