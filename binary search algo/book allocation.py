def isallowed(arr,mid,m):
    pages = 0
    student = 0
    for i in range(len(arr)):
        student+=1
        if pages+arr[i]<=mid:
            pages +=arr[i]
        else:
            pages = arr[i]
            student +=1
            if student >2:
                return False
    return True
        




def allocate(arr, m):
    start = 0
    end = len(arr)

    while start<=end:
        mid = start+(start+end)//2
        if isallowed(arr, mid, m ):
            end = mid-1
        else:
            start = mid+1
    return mid
arr = [10,20,30,40]
allocate(arr,2)

    