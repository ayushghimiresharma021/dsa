def detection(head):
    if head == None:
        return
    first = head
    arr = []
    while (first):
        if first in arr:
            return True
        arr.append(first)
        first = first.next
    return False


