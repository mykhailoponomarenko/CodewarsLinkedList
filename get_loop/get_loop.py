def loop_size(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next     
        fast = fast.next.next  
        if slow == fast:
            length = 1  
            fast = fast.next 
            while slow != fast:
                fast = fast.next  
                length += 1  
            return length
    return 0