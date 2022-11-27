## 1.Using recurion and memosiation


import sys
def minimumdp(num,x,dp):
    if x == 0:
        return 0
    if x<1:
        return sys.maxsize
    if dp[x]!=-1:
        return dp[x]
    mini = sys.maxsize
    for i in num:
        ans = minimumdp(dp,x-i,dp)
        if ans != sys.maxsize:
            mini =min(mini,1+ans)
    dp[x] = mini
    return dp[x]
##2.using table
def mincoinsusingtable(num,x):
    dp = [sys.maxsize]*x
    dp[0] = 0
    for i in range(x):
        for value in num:
            if i-value>=0 and dp[i]!=sys.maxsize:
                dp[i] = min(dp[i],1+dp[i-value])

##3.space complexity == o(1)


