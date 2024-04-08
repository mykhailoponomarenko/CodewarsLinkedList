class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
def sorted_insert(head, data):
    if head is None or head.data >= data:
        a = Node(data)
        a.next = head
        print(a)
        return a
    a = Node(data)
    cur = head
    while cur.next is not None and cur.next.data < data:
        cur = cur.next
    a.next = cur.next
    cur.next = a
    return head
def stringify(node):
    data = []
    while node is not None:
        data.append(str(node.data))
        node = node.next
    data.append('None')
    return ' -> '.join(data)
print(stringify(sorted_insert(Node(1, Node(2, Node(3))), 4)))
