# find pivot element in an rotated array
def pivot(arr):
    low =0
    high = len(arr)-1
    while low<high:
        mid = low+(low+high)//2
        if arr[low]<=arr[mid]:
            low = mid+1
        else:
            high = mid 
def searchInRotatedArray(arr,key,low,high):
    mid  = (low+high)//2
    if arr[mid]==key:
        return mid
    if arr[mid]>=arr[low]:
        if key>=arr[low] and key<=arr[mid]:
            return searchInRotatedArray(arr,key,low,mid-1)
        return searchInRotatedArray(arr,key,mid+1,high)
    elif arr[mid]<=key and arr[high]>=key:
        return searchInRotatedArray(arr,key,mid+1,high)
    return searchInRotatedArray(arr,key,low,mid-1)



            
            

