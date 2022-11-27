class Node():
    def __init__(self,val):
        self.val=val
        self.next = None
        self.random = None


class linked_linked:
    def __init__(self):
        self.head = None
    def insertattail(self,head,tail,d):
        new_node = Node(d)
        if head ==None:
            head = new_node
            tail = new_node
            return 
        else:
            tail.next = new_node
            head = new_node
    

    def cloned(self,head1):
        cloned_head = None
        cloned_tail = None
        temp = head1
        while temp:
            self.insertattail(cloned_head,cloned_tail,temp.val)
            temp = temp.next
        oldtonew = {}
        temp = head1
        temp1 = cloned_head
        while temp and temp1:
            oldtonew[temp] = temp1
            temp = temp.next
            temp1 = temp1.next
        temp = head1
        temp2 = cloned_head
        while temp:
            temp2.random = oldtonew[temp.random]
            temp =temp.next
            temp2 = temp2.next
        return cloned_head
            





