def find(m,arr,n):
    pages = 0
    count = 0
    for i in arr:
        if pages<=m:
            pages+=i
        else:
            count+=1
            if count>n and pages>=m:
                return False
            
            pages=i
    return True
def book(arr,k):
    low = 0
    maxi = 0
    for i in arr:
        maxi+=i
    high = maxi
    ans = -1
    while low<high:
        mid = low+(low+high)//2
        if find(mid,arr,k):
            ans = mid
            high = mid-1
        else:
            end =mid+1
    return ans


            


        
    
