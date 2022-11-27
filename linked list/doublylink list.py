class Node:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None
class doublylinked:
    def __init__(self):
        self.head = None
    def push(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        new_node.next  = self.head
        self.head.prev = new_node
        self.head = new_node
    def nthnode(self,prev,new_data):
        last = self.head 
        new_node = Node(new_data)
        while last.val == prev:
            last = last.next
        new_node.next = last.next
        last.next = new_node
        new_node.prev = last
    def deletion(self,data):
        last = self.head
        if last.val == data:
            self.head = last.next
            last.next.prev = None
            return 


        while last.val==data:
            last = last.next
        if last.next==None:
            last = last.prev
            last.next = None
            return

        p = last.prev
        n = last.next
        p.next = next
    def printing(self):
        last  = self.head
        while last:
            print(last.val,end=' ')
            last = last.next
d = doublylinked()
d.push(1)
d.push(2)
d.push(3)
d.push(4)
d.push(5)
d.printing()
d.deletion(4)
print()
d.printing()
        



        
        

        
            

