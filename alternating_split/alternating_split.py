class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
def alternating_split(head):
    if not head or not head.next:
        raise ValueError
    i = 0
    lst1 = Node()
    lst2 = Node()
    lst_1_c = lst1
    lst_2_c = lst2
    while head is not None:
        if i % 2 == 0:
            lst1.next = Node(head.data)
            lst1 = lst1.next
        else:
            lst2.next = Node(head.data)
            lst2 = lst2.next
        head = head.next
        i += 1
    return Context(lst_1_c.next, lst_2_c.next)