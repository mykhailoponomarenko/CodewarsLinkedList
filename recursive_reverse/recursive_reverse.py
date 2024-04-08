class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
def reverse(head):
    if head is None or head.next is None:
        return head
    def func(cur, prev):
        if cur is None:
            return prev
        next_node = cur.next
        cur.next = prev
        return func(next_node, cur)
    return func(head, None)