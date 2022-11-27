def palindrom(head):
    last = head 
    arr = []
    while last:
        arr.append(last.val)
        last = last.next
    start = 0
    end = len(arr)
    while start<=end:
        if arr[start] == arr[end]:
            start+=1
            end-=1
        else:
            return False
    return True