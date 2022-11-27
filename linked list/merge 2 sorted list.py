def merge2sorted(head1,head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    temp = None

    while head1 and head2:
        if head1.val<head2.val:
            temp = head1
            temp.next = merge2sorted(head1.next,head2)
        else:
            temp = head2
            temp.next = merge2sorted(head1,head2)
    return temp
        