def Node():
    def __init__(self,val):
        self.val = val 
        self.next = None

def add(head1,head2):
    first = head1
    last = head2
    ans = None
    sum = carry
    arr = []
    while first and last :
        
        sum = first.val+last.val+carry
        carry = int(sum//2)
        digit = sum%10
        first = first.next
        last = last.next
    while first:
        sum = first.val+carry
        carry = int(sum//2)
        digit = sum%10
        first = first.next
    while last:
        sum = last.val+carry
        carry = int(sum//2)
        digit = sum%10
        last =last.next
    while  carry!=0:
        sum = carry
        digit = sum/10
        carry = sum%10


        



def reverse_linked(head1):
    curr = head1
    prev = None
    next  = None
    while curr:
        next = curr.next 
        curr.next = prev
        orev = curr
        curr = next
    return prev
def sumofTwo(head1,head2):
    h1 = reverse_linked(head1)
    h2 = reverse_linked(head2)

    ans = add(h1,h2)

    ans = reverse_linked(ans)