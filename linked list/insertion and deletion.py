class Node:
    def __init__(self,data):
        self.val =data
        self.next = None
class Linked_list:
    def __init__(self):
        self.head = None
    def insertion(self,val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        new_node.next = self.head
        self.head = last
    def inserttionbetween(self,prev,next):
        last = self.head
        new_node = Node(next)
        while last.val == prev:
            last =last.next
        new_node.next = last.next
        last.next = new_node
    def deletion(self,prev):
        last = self.head
        if last!=None:
            if last.data == prev:
                self.head = last.next
                last = None
                return 
        while last.next != None :
            if last.next.data == prev:
                break
            last = last.next
        last.next = last.next.next
        last = None
        

        


        