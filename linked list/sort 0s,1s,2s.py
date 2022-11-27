def sorted(head):
    if head ==None:
        return 
    first =head 
    count = []*3
    while first:
        count[first.val]+=1
        first = first.next
    last = head
    i=0
    while last:
        if count[i] == 0:
            i+=1
        else:
            last.val = i
            count[i]-=1
            last = last.next
            




