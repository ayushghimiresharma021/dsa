def combination(arr,dp,target):
    if target==0:
        return 1
    if target<0:
        return 0
    if dp[target]!=-1:
        return 
    count = 0
    for i in range(len(arr)):
        count+=combination(arr,dp,target-arr[i])
    dp[target] =count
    return dp[target]
def tablecombination(arr,target):
    dp = [-1 for i in range(target+1)]
    dp[0] = 1
    for i in range(target+1):
        for j in range(len(arr)):
            if i-arr[j]>=0:
                dp[i]+=dp[i-arr[j]]

        


