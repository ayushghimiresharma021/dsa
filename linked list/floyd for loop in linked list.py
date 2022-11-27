def floyd(head):
    slow = head
    fast = head
    while fast :
        fast =fast.next 
        if fast:
            fast = fast.next
        slow = slow.next
        if slow == fast:
            return True
    
        
