def firstAppearance(arr,n,k):
    low = 0 
    high = n-1
    
    while(low<=high):
        mid = low+(low+high)//2
        if arr[mid]==k:
            occ = mid
            low = mid-1
        elif arr[mid]<k:
            low = mid+1
        else:
            high = mid-1
    return occ 
def lastoccurance(arr,n,k):
    low = 0 
    high =n-1
    while(low<=high):
        mid = low+(low+high)//2
        if arr[mid]==k:
            occ = mid
            low = mid+1
        elif arr[mid]<k:
            low =mid+1
        else:
            high = mid-1
def totalNumber(arr,n,k):
    f = firstAppearance(arr,n,k)
    last = lastoccurance(arr,n,k)

    return last-f
