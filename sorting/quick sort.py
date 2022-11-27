def quicksort(arr,low,high):
    
    pivot = arr[high]
    j =low
    for i in range(low,high):
        if arr[i]<=pivot:
            arr[i],arr[j]=arr[j],arr[i]
            j+=1
        arr[j],arr[high] = arr[high],arr[j]
    return j
def quick(arr,low,high):
    if low<high:
        p  = quicksort(arr,low,high)
        
        quick(arr,low,p-1)
        quick(arr,p,high)
array = [10, 7, 8, 9, 1, 5]
quick(array,0,len(array)-1)
print(array)

