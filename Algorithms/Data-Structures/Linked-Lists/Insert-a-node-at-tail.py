def insertNodeAtTail(head, data):
    node = SinglyLinkedListNode(data)
    if not head:
        return node
    ptr = head
    while head.next:
        head = head.next
        
    head.next = node
    return ptr