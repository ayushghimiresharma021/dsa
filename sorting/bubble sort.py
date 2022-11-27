def bubble_sort(arr,n):
    swapped = False
    for i in range(n-1):
        for j in range(n-i):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped = True
        if swapped == False:
            break
arr = [2,3,4]
        
            
