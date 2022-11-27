def selectionsor(arr):
    n = len(arr)-1
    for i in range(n-1):
        midindex = i
        for j in range(i+1,n):
            if arr[midindex]>arr[j]:
                midindex = j
        arr[midindex], arr[i] = arr[i], arr[midindex]
