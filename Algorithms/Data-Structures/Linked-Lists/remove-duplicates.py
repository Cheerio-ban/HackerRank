def removeDuplicates(llist):
    # Write your code here
    curr = llist
    prev = None
    
    if curr == None or curr.next == None:
        return llist
    else:
        prev = curr
        curr = curr.next
    while curr:
        if prev.data == curr.data:
            prev.next = curr.next
            curr = curr.next
        else:
            prev = prev.next
            curr = curr.next
    return llist
