class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
def swap_pairs(head):
    if not head or not head.next:
        return head
    last = None
    cur = head
    while cur and cur.next:
        a = cur.next
        cur.next = a.next
        a.next = cur
        if last is None:
            head = a
        else:
            last.next = a
        last = cur
        cur = cur.next
    return head