def invadeRecur(arr):
    n = len(arr)
    first =[0]
    last =[0]
    dp1 = [-1]*(n+1)
    dp2 = [-1]*(n+1)
    for i in range(n):
        if i!=0:
            last.append(arr[i])
        if i != n-1:
            first.append[arr[i]]
    last.reverse()
    first.reverse()
    return max(maximumSum(first,len(first)-1,dp1),maximumSum(last,len(last)-1,dp2))
    



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
    