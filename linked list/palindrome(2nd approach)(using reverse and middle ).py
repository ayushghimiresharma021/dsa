def comparsion(head1,head2):
    temp1 = head1
    temp2 =head2
    while temp1 and temp2:
        if temp1.val!=temp2.val:
            return False
        temp1=temp1.next
        temp2 = temp2.next
    if temp1!=None and temp2!=None:
        return True
    return False
def middle(head):
    slow  =head
    fast = head
    while (fast.next!=None and fast):
        slow = slow.next
        prev_of_slow = slow
        fast =fast.next.next
    second_half = slow
    prev_of_slow.next = None
    second_half = reverse(second_half)
    com  = comparsion(head,second_half)
    return com
def reverse(head):
    last = head 
    temp = None
    next = None
    curr = head

    while curr :
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev 
    

        
    
    