def merge(arr,low,high):
    mid =(low+high)//2
    l_index = mid-low+1
    r_index = high-mid
    l = [0]*l_index
    r = [0]*r_index
    start = low
    for i in range(l_index):
        l[i] = arr[start]
        start+=1
    start = mid+1
    for j in range(r_index):
        r[j] = arr[start]
        start+=1
    start = low
    index1 = 0
    index2 = 0
    while (index1<l_index and index2<r_index):
        if l[index1]<r[index2]:
            arr[start] = l[index1]
            index1+=1
        else:
            arr[start] = r[index2]
            index2+=1
        start+=1
    while (index1<l_index):
        arr[start]=l[index1]
        start+=1
        index1+=1
    while (index2<r_index):
        arr[start] = r[index2]
        start+=1
        index2+=1





def mergessort(arr,low,high):
    if low>=high:
        return 
    mid = (low+high)//2

    mergessort(arr,low,mid)
    mergessort(arr,mid+1,high)
    merge(arr,low,high)

arr = [9,8,7,1,2,3,0]
mergessort(arr,0,len(arr)-1)
print(arr)