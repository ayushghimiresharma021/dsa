import sys

def cut(rod,x,y,z,dp):
    if rod == 0:
        return 0
    if rod<0:
        return -(sys.maxsize)
    if dp[rod]!=-1:
        return dp[rod]

    rod_x = cut(rod-x,x,y,z,dp)+1
    rod_y = cut(rod-y,x,y,z,dp)+1
    rod_z = cut(rod-z,x,y,z,dp)+1

    dp[rod] = max(rod_x,rod_y,rod_z)
    return dp[rod]
def cutinto(rod,x,y,z):
    dp = [-1]*(rod+1)
    dp[0] = [0]
    for i in range(len(dp)):
        if i-x>=0:
            dp[i] = max(dp[i],dp[i-x]+1)
        if i-y>=0:
            dp[i] = max(dp[i],dp[i-y]+1)
        if i-z>=0:
            dp[i] =max(dp[i].dp[i-z]+1)
    return dp[rod]
    

